from functions import store,similarity,store_JSON
from utils import read_doc,chunk_data
import google.generativeai as genai
from chain import generate
import json
# from pinecone import Pinecone

# root = './assets/'
# document = read_doc(root)
# docs = chunk_data(document)

# store(docs,namespace="NITKKR")


json_file_path = './assets/student_roll.json'
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

chunk = chunk_data(data)
store(chunk,namespace="NITKKR")





