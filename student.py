import google.generativeai as genai
from rapidfuzz import fuzz
import json

genai.configure(api_key="AIzaSyCqS4dnLO_qKB4aqrh3VZPh1wfEOyUN75E")

# Load student data
with open('./assets/student_roll.json') as f:
    data = json.load(f)

def get_class(text):
    model = genai.GenerativeModel('gemini-1.5-flash',
                                  generation_config={"response_mime_type": "application/json"})
    prompt = """
    Extract the section, name, and roll number from the following text, where sections look like "IT-A", and roll numbers are 8 digits, like "12213149".
    """ + text

    response = model.generate_content(prompt)
    try:
        result = json.loads(response.text)  
    except json.JSONDecodeError:
        result = None
    return result

# Function to search for the best match
def search_student(prompt):
    # First try to extract with Generative AI
    extracted_data = get_class(prompt)
    if extracted_data:
        roll_number = extracted_data.get('roll_number')
        name = extracted_data.get('name')
        main_section = extracted_data.get('section')
    else:
        # Fallback manual extraction if Generative AI fails
        keywords = prompt.lower().split()
        roll_number = next((word for word in keywords if word.isdigit()), None)
        name = " ".join([word.capitalize() for word in keywords if word.isalpha() and len(word) > 2])
        main_section = next((word for word in keywords if "-" in word), None)

    def names_match(student_name, query_name):
        student_words = set(student_name.lower().split())
        query_words = set(query_name.lower().split())
        return query_words <= student_words  

    # Search for an exact match with flexible name matching
    for year_data in data:
        for section in year_data['sections']:
            for student in section['students']:
                if ((not roll_number or student["roll_number"] == roll_number) and
                    (not name or names_match(student["name"], name)) and
                    (not main_section or student["main_section"].lower() == main_section.lower())):
                    return str(student) 

    return "No matching student found."


# prompt = "Find student named pradeep korra with roll number 12213155 in section it-b"
# result = get_class(prompt)
# result1 = search_student(prompt)

# print(result)
# print(result1)