import os, importlib.util, settings
commands={}
pluglist=[]
def load_plugins():
    errors=[]
    plugin_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), settings.PLUGINS_FOLDER)
    plugin_files = [f for f in os.listdir(plugin_dir) if f.endswith('.plug.py') and f not in settings.DISABLED_PLUGINS]
    for plugin_ in plugin_files:
        pluglist.append(plugin_)
        plugin_name = plugin_[:-8]
        spec = importlib.util.spec_from_file_location(plugin_name, os.path.join(plugin_dir, plugin_))
        temp_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(temp_module)
        for k in temp_module.return_cmdlist():
            if k in commands.keys():
                errors.append(f"{temp_module.plugin_name} (Version {temp_module.plugin_version} / Made by {temp_module.plugin_author}) has duplicate command {k} with {commands[k].plugin_name} (Version {commands[k].plugin_version} / Made by {commands[k].plugin_author}")
            commands[k] = temp_module
    return errors

test=load_plugins()

print(f"{len(pluglist)} Plugins Loaded, {len(commands.keys())} Commands Loaded.")
print(f"Found total {len(test)} errors.")
print('\n'.join(test))