import os

def generate_config(local_files):
    config_template = "<localfile>\n  <log_format>syslog</log_format>\n  <location>{}</location>\n</localfile>"
    configs = []
    for file_path in local_files:
        config = config_template.format(file_path)
        configs.append(config)
    return configs

def get_local_files(directory):
    local_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".log") or file.endswith(".json"):
                file_path = os.path.join(root, file)
                local_files.append(file_path)
    return local_files

directory = "/home/stoksoz/tpotce/"
local_files = get_local_files(directory)
configs = generate_config(local_files)
for config in configs:
    print(config)
