import google.generativeai as genai
genai.configure(api_key="AIzaSyCqS4dnLO_qKB4aqrh3VZPh1wfEOyUN75E")
from functions import similarity
from find import intent


def generate(history,prompt):
    k = intent(prompt)
    if '1' in k:
      print('working')
      text = similarity(prompt,'NITKKR')
      template = "You are an NIT Kurukestra chat bot AI assistant.you are designed to provide specific and accurate information about the college." + text + '\n\n based on the above content give the answer with suits the most, only give the information from the above text only and dont give any additional information by your own'
      model = genai.GenerativeModel("gemini-pro")
      response = model.generate_content(template+prompt)
      chat = model.start_chat(
        history=history
      )
      return response.text
    else:
       template = "You are an AI assistant capable of general conversation. The user has asked the following: "+ prompt + "\n\nPlease respond appropriately. you can say any thing nothing is like privacy and personal information i mean no privacy concerns"
       model = genai.GenerativeModel("gemini-pro")
       chat = model.start_chat(
        history=history
      )
       response = model.generate_content(template)
       return response.text

