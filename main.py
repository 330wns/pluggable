from _typeshed import importlib
from discord import template
import discord
import settings
import os
import importlib.util
from datetime import datetime

bot=discord.Client(intents=discord.Intents.all())
commands={}
plugincount=0

#region some things
class DuplicateCommandError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
class PluginErrorCrashOut(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
#endregion

#region functions
def log(msg):
    with open('bot.log','a')as f:
        f.write(f"[{datetime.now.strftime("%Y-%m-%d %H-%M-%S")}] {msg}\n")
        f.close()

def load_plugins():
    plugin_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), settings.PLUGINS_FOLDER)
    plugin_files = [f for f in os.listdir(plugin_dir) if f.endswith('.plug.py') and f not in settings.DISABLED_PLUGINS]
    plugincount=len(plugin_files)
    for plugin_ in plugin_files:
        plugin_name = plugin_[:-8]
        spec = importlib.util.spec_from_file_location(plugin_name, os.path.join(plugin_dir, plugin_))
        temp_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(temp_module)
        for k in temp_module.return_cmdlist():
            if k in commands.keys():
                if settings.SAVE_LOGS:
                    log(f"{temp_module.plugin_name} (Version {temp_module.plugin_version} / Made by {temp_module.plugin_author}) has duplicate command {k} with {commands[k].plugin_name} (Version {commands[k].plugin_version} / Made by {commands[k].plugin_author})")
                raise DuplicateCommandError(f"{temp_module.plugin_name} (Version {temp_module.plugin_version} / Made by {temp_module.plugin_author}) has duplicate command {k} with {commands[k].plugin_name} (Version {commands[k].plugin_version} / Made by {commands[k].plugin_author})")
            commands[k] = temp_module
#endregion

@bot.event
async def on_ready():
    print("ready")
    print(f"{plugincount} Plugins loaded.")
    print(f"{len(commands.keys())} Commands loaded.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    cmd=message.content.split()[0]
    if cmd=='!plugin' and not settings.DISABLE_PLUGINS_COMMAND:
        await message.channel.send(f"{plugincount} Plugins & {len(commands.keys())} Commands loaded.")
    elif cmd in commands.keys():
        res=await commands[cmd].process_cmd(bot, message)
        if res != True:
            print(f"Plugin({commands[cmd].plugin_name} Version {commands[cmd].plugin_version} by {commands[cmd].plugin}) responded a error: {cmd}")
            if settings.SAVE_LOGS:
                log(f"Plugin({commands[cmd].plugin_name} Version {commands[cmd].plugin_version} by {commands[cmd].plugin}) responded a error: {cmd}")
            if settings.CRASH_BOT_AFTER_PLUGIN_ERROR:
                raise PluginErrorCrashOut(res)
bot.run(settings.token)
