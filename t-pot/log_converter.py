import json
import os
import time

# Function to rename JSON fields for multiple input files
def rename_json_fields_multiple(input_files, output_file, logs_per_second):
    try:
        # Open the output JSON file in append mode
        with open(output_file, 'a') as f_output:
            while True:
                # Iterate over input files
                for input_file in input_files:
                    # Get the base name of the input file without extension
                    base_name = os.path.splitext(os.path.basename(input_file))[0]

                    # Open the current input file
                    with open(input_file, 'r') as f_input:
                        # Process each line in the input file
                        for line in f_input:
                            # Parse JSON from the current line
                            data = json.loads(line)
                            
                            # Iterate over the keys in the JSON object
                            for key in list(data.keys()):
                                # Generate a new key by appending '_{basename}'
                                new_key = f"{key}_{base_name}"
                                data[new_key] = data.pop(key)
                            
                            # Write the modified data to the output file
                            json.dump(data, f_output)
                            # Add a newline after each JSON object
                            f_output.write('\n')
                            
                            # Sleep to achieve the desired logs per second
                            time.sleep(1 / logs_per_second)

                print("Inserted 1000 logs into the output file.")
    except Exception as e:
        print(f"Error: {e}")

# Paths to input JSON files
input_files = [
    "/home/stoksoz/tpotce/data/p0f/log/p0f.json",
    "/home/stoksoz/tpotce/data/another_folder/another_file.json",
]

# Path to output JSON file
output_file = "/home/stoksoz/tpotce/data/suricata/log/eve.json"

# Number of logs to insert per second
logs_per_second = 1000

# Call the function to rename JSON fields for multiple input files
rename_json_fields_multiple(input_files, output_file, logs_per_second)
