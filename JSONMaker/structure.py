import json
from collections import defaultdict
import os 

# Load student data from your JSON file
input_file = os.path.join("4.json")
with open(input_file, 'r') as f:
    data = json.load(f)  # Parse the JSON file into a Python object

# Main header info (can be changed as needed)
year = "2024"

# Function to group students by main section
def group_students_by_section(data):
    sections = defaultdict(list)  # Create a dictionary where each section will store student data
    for student in data:
        sections[student["main_section"]].append(student)
    return sections

# Function to build the desired JSON structure
def build_class_structure(students_data, year):
    grouped_sections = group_students_by_section(students_data)
    section_list = []

    for section_name, students in grouped_sections.items():
        # Get branch info and representative based on the section
        section_branch = students[0]["branch"]  # All students in this section will have the same branch
        section_strength = len(students)
        
        # Prepare the section structure
        section = {
            "className": section_name,
            "strength": section_strength,
            "branch": section_branch,
            "students": [
                {
                    "roll_number": student["roll_number"],
                    "name": student["name"],
                    "main_section": student["main_section"],
                    "sub_section": student["sub_section"]
                }
                for student in students
            ]
        }
        section_list.append(section)

    # Create the final structure
    final_structure = {
        "year": year,
        "sections": section_list
    }
    
    return final_structure

# Create the structured data
structured_data = build_class_structure(data, year)

# Output the structured data as JSON
output_file = 'structured_students.json'
with open(output_file, 'w') as f:
    json.dump(structured_data, f, indent=4)

print(f"Structured data saved to {output_file}")
