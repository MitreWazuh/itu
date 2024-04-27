import csv
import json

# Function to convert CSV to JSON line format
def csv_to_json_line(header_row, data_row):
    # Create a dictionary using the header row as keys and data row as values
    json_data = {header_row[i]: data_row[i] for i in range(min(len(header_row), len(data_row)))}
    # Add the "loggenerator" tag at the beginning
    json_data = {"loggenerator": "redteam", **json_data}
    return json.dumps(json_data)

# Function to process CSV file and write JSON lines to a file
def process_csv_file(csv_file_path, output_file_path):
    with open(csv_file_path, 'r') as csv_file, open(output_file_path, 'w') as json_file:
        csv_reader = csv.reader(csv_file)
        # Read the header row
        header_row = next(csv_reader)
        for row in csv_reader:
            # Convert each row to JSON line format using header row as JSON keys
            json_line = csv_to_json_line(header_row, row)
            # Write JSON line to the output file
            json_file.write(json_line + '\n')
            print(json_line)

# Example usage: Convert /home/stoksoz/1.csv file to JSON once
if __name__ == "__main__":
    input_csv_file = "/home/stoksoz/1.csv"
    output_json_file = "/home/stoksoz/atom.json"
    process_csv_file(input_csv_file, output_json_file)
