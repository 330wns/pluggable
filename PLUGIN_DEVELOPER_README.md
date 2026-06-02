thank you for making pluggable plugins:3
this is the document to show how to make pluggable plugins!

# the plugin should follow this format:
1. plugin must end with .plug.py

2. you need to add plugin details. Pluggable supports 3 details:
    * plugin_name: The name of the plugin
    * plugin_author: The author of the plugin
    * plugin_version: The version of the plugin
    ALL 3 is mandatory!

3. it needs return_cmdlist() function. (Not ASYNC)
    This function must return all the list of the plugin's command. 
    You can choose any command prefix! You need to put command with prefix in the list!
    example format: ['!cmd1','!cmd2','!cmd3']
    This is a mandatory function.

4. it needs process_cmd() function. (IS ASYNC)
    This is the function that will handle every command!
    When your plugin is used, main.py will do await your_plugin.process_cmd(bot,message) in your plugin.
    You can see the message info like : message.author, message.channel, message.content, message.guild etc.
    You will return True if the command was processed successfully, or any error messages if it failed! (It will show the error to the user.)
    This is a mandatory function.

this is all mandatory format for the plugin! you can add any other function or codes u want:3

# TIPS:
1. Enjoy
2. good job