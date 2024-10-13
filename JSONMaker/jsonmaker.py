import pdfplumber
import json
import os

pdf_file_path = os.path.join("assets", "4th year.pdf")

output_json_path = os.path.join("4st_JSON.json")

def get_branch_name(main_section):
    branch_mapping = {
        "ce": "Civil Engineering",
        "me": "Mechanical Engineering",
        "pi": "Production Engineering",
        "cs": "Computer Engineering",
        "it": "Information Technology",
        "ee": "Electrical Engineering",
        "ec": "Electronics and Communication Engineering"
    }
    if main_section:
        main_section_prefix = main_section.split('-')[0].lower()
        return branch_mapping.get(main_section_prefix)
    else:
        return "Unknown"

def extract_data_from_pdf(pdf_file_path):
    data = []
    with pdfplumber.open(pdf_file_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table[1:]: 
                    if len(row) >= 4:
                        main_section = row[3]
                        branch = get_branch_name(main_section) 
                        data.append({
                            "roll_number": row[1],
                            "name": row[2],
                            "main_section": main_section,
                            "sub_section": row[4],
                            "branch": branch  
                        })
    return data

def convert_to_json(data):
    return json.dumps(data, indent=4)

data = extract_data_from_pdf(pdf_file_path)

data_json = convert_to_json(data)

with open(output_json_path, "w") as json_file:
    json_file.write(data_json)

print(f"Data extracted and saved to '{output_json_path}'.")
