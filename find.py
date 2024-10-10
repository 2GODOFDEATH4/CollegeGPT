import google.generativeai as genai
genai.configure(api_key="AIzaSyClpiiKMB7BtN3Ccdvu99URToNvu6CVBr0")
from functions import similarity

#1yes,0No

def intent(prompt):
    text = prompt
    template = "Tell me whether the query is related to college information it can be anything realted to nit kurukeshtra or not?\n\n" + text + '\n\n if the query is related to college just give the reply as 1 if is not then tell me 0 just only give me one word asnwer 1 or 0 thats it'
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(template+prompt)
    return response.text


