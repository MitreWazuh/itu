import re
import json

def parse_access_log(log_file):
    log_entries = []
    with open(log_file, 'r') as f:
        for line in f:
            pattern = r'^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+) (\S+)" (\d{3}) (\d+|-)'
            match = re.match(pattern, line)
            if match:
                entry = {
                    'loggenerator': 'dvwa',  # Added loggenerator tag
                    'ip': match.group(1),
                    'date': match.group(4),
                    'method': match.group(5),
                    'url': match.group(6),
                    'status': match.group(7),
                    'bytes': match.group(8)
                }
                log_entries.append(entry)
    return log_entries

def save_to_json(log_entries, json_file):
    with open(json_file, 'w') as f:
        for entry in log_entries:
            json.dump(entry, f)
            f.write('\n')

log_file_path = '/home/stoksoz/access.log'
json_file_path = '/home/stoksoz/access.json'

parsed_entries = parse_access_log(log_file_path)

save_to_json(parsed_entries, json_file_path)

print("Conversion complete. JSON file saved at:", json_file_path)
