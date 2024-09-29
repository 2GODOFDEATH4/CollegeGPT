from functions import store,similarity
from utils import read_doc,chunk_data
import google.generativeai as genai
from chain import generate
# from pinecone import Pinecone

# root = './assets/'
# document = read_doc(root)
# docs = chunk_data(document)

# store(docs,namespace="NITKKR")

# print(similarity('if have a qurery related academic section what should i do?','NITKKR'))
# print(similarity('if i have any query related to academics?','NITKKR'))

  

print(generate('courses provided by nit kurukestra'))



