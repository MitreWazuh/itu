import re
import json

# Define the path to the audit log file
audit_log_path = "/var/log/audit/audit.log"

# Define the path to the syslog file
syslog_path = "/var/ossec/logs/active-responses.log"


# Regular expression pattern to match log entries
log_pattern = re.compile(r'type=(\w+)\s+msg=audit\((\d+\.\d+):(\d+)\):(.*)')

def parse_log_entry(entry):
    """
    Parse a single log entry and convert it to JSON format.
    """
    match = log_pattern.search(entry)
    if match:
        log_type = match.group(1)
        audit_timestamp = match.group(2)
        audit_id = match.group(3)
        rest_of_entry = match.group(4).strip()

        # Split the rest of the entry by spaces and create key-value pairs
        kv_pairs = [kv.split('=') for kv in rest_of_entry.split()]

        # Construct a dictionary with the log entry information
        log_dict = {
            "logsource": "auditd", # Add logsource tag
            "type": log_type,
            "audit_timestamp": audit_timestamp,
            "audit_id": audit_id,
            "details": {kv[0]: kv[1] for kv in kv_pairs}
        }
        return log_dict
    else:
        return None

def convert_to_json(log_entries):
    """
    Convert parsed log entries to JSON format.
    """
    json_logs = []
    for entry in log_entries:
        json_logs.append(json.dumps(entry))
    return json_logs

def main():
    # Read audit log file
    with open(audit_log_path, 'r') as audit_log_file:
        audit_logs = audit_log_file.readlines()

    # Parse log entries
    parsed_logs = [parse_log_entry(entry) for entry in audit_logs]

    # Convert parsed logs to JSON format
    json_logs = convert_to_json(parsed_logs)

    # Append JSON logs to syslog file
    with open(syslog_path, 'a') as syslog_file:
        for log in json_logs:
            syslog_file.write(log + '\n')

if __name__ == "__main__":
    main()
