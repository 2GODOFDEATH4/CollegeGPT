import google.generativeai as genai
genai.configure(api_key="AIzaSyDGJFFUTdcyFzaIcgS698-I7ZvZiWK0WuI")

def memory(history,prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(
        history=history
    )
    response = chat.send_message(prompt)
    return response.text


