import json
import os 

# Function to filter out entries with null or empty roll_number
def filter_invalid_entries(data):
    return [student for student in data if student["roll_number"] not in (None, "",".oN\nlloR")]

# Read JSON data from a file
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Write filtered JSON data to a file
def save_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Main function to handle filtering
def filter_json_file(input_file_path, output_file_path):
    # Load data from the input JSON file
    data = load_json_file(input_file_path)
    
    # Filter the data
    filtered_data = filter_invalid_entries(data)
    
    # Save the filtered data to the output JSON file
    save_json_file(filtered_data, output_file_path)

# Example usage
input_file = os.path.join("4st_JSON.json")
output_file = 'filtered_students.json'  # Path to the output JSON file

# Filter the JSON file
filter_json_file(input_file, output_file)

print(f"Filtered data saved to {output_file}")
