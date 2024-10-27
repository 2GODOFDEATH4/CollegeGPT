import google.generativeai as genai
genai.configure(api_key="AIzaSyCqS4dnLO_qKB4aqrh3VZPh1wfEOyUN75E")
from functions import similarity

#1yes,0No

def intent(prompt):
    text = prompt
    template = "Tell me whether the query is related to college information it can be anything realted to nit kurukeshtra or not?\n\n" + text + '\n\n if the query is related to college just give the reply as 1 and i f the query is related to college and if the user is mentioned any roll number or sub section or main section or branch or any 2 or 3 of them and asking for the other information like giving his roll number and section and asking for hs/her name or giving his section and name and asking for his roll number, if the user query is like this return 2, if is not then tell me 0 just only give me one word asnwer 1 or 0 or 2 thats it'
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(template+prompt)
    return response.text


