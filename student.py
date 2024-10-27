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
        result = json.loads(response.text)  # Expecting JSON-formatted result
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

    best_match = None
    highest_score = 0

    # Search JSON data for the best match
    for year_data in data:
        for section in year_data['sections']:
            for student in section['students']:
                # Calculate similarity score
                score = 0
                if roll_number:
                    score += fuzz.ratio(student["roll_number"], roll_number) * 1.5
                if name:
                    score += fuzz.partial_ratio(student["name"], name)
                if main_section:
                    score += fuzz.ratio(student["main_section"], main_section)

                if score > highest_score:
                    highest_score = score
                    best_match = student

    return best_match or "No matching student found."


prompt = "Find student named Kushagra with roll number 124101001 in section CE-A"
result = search_student(prompt)
print(type(result))
