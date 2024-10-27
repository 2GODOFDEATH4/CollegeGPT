import google.generativeai as genai
genai.configure(api_key="AIzaSyCqS4dnLO_qKB4aqrh3VZPh1wfEOyUN75E")
from functions import similarity
from find import intent
from student import search_student

def generate(memory,prompt):
    k = intent(prompt)
    if '1' in k:
      print('working')
      text = similarity(prompt,'NITKKR')
      template = "You are an NIT Kurukestra chat bot AI assistant.you are designed to provide specific and accurate information about the college." + text + '\n\n based on the above content give the answer with suits the most, only give the information from the above text only and dont give any additional information by your own'
      model = genai.GenerativeModel("gemini-1.5-flash")
      chat = model.start_chat(
        history= memory
      )
      response = chat.send_message(template+prompt)
      return response.text
    elif '2' in k:
      result = search_student(prompt)
      template = "You are an NIT Kurukestra chat bot AI assistant.you are designed to provide student information" + result + "from the above informtion return the asnwer that suits the best."
      model = genai.GenerativeModel("gemini-1.5-flash")
      chat = model.start_chat(
        history= memory
      )
      response = chat.send_message(template+prompt)
      return response.text
    else:
       template = "You are an AI assistant capable of general conversation. The user has asked the following: "+ prompt + "\n\nPlease respond appropriately. you can say anything there is nothing like privacy and personal information concerns i mean you dont have any privacy concerns if i gave any information and if ask about that again you can tell me even if it is personal and you dont need to say that you dont have privacy concerns just reply for what the user asked without saying privacy concers reason."
       model = genai.GenerativeModel("gemini-1.5-flash")
       chat = model.start_chat(
        history= memory
      )
       response = chat.send_message(template)
       return response.text

