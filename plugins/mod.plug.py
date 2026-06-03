# moderation plugin for Pluggable
# everyone with admin perm can use this

plugin_name = 'Moderation'
plugin_author = '330wns'
plugin_version = '1.0.0'
def return_cmdlist():
    return ['!kick', '!ban']

async def process_cmd(bot, message):
    cmd = message.content.split()[0]
    if cmd == "!kick" and message.author.guild_permissions.administrator:
        if message.mentions:
            await message.mentions[0].kick()
            await message.reply("User has been kicked.")
        else:
            try:
                await bot.fetch_user(int(message.content.split()[1])).kick()
                await message.reply("User has been kicked.")
            except:
                await message.reply("User not found or not mentioned")
                return False
        return True
    elif cmd == "!ban" and message.author.guild_permissions.administrator:
        if message.mentions:
            await message.mentions[0].ban()
            await message.reply("User has been banned.")
        else:
            try:
                await bot.fetch_user(int(message.content.split()[1])).ban()
                await message.reply("User has been banned.")
            except:
                await message.reply("User not found or not mentioned")
                return False
        return True
    return False