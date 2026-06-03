# 1st plugin for Pluggable
# Commands: !say

plugin_name = 'Say'
plugin_author = '330wns'
plugin_version = '1.0.0'
def return_cmdlist():
    return ['!say']

async def process_cmd(bot, message):
    if message.content.split()[0] == '!say':
        await message.channel.send(message.content[5:])
        return True
    return False