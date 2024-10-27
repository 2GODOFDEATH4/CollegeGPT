from functions import store,similarity,store_json
from utils import read_doc,chunk_data,chunk_json
import google.generativeai as genai
from chain import generate
import json
from pinecone import Pinecone

root = './assets/'
document = read_doc(root)
docs = chunk_data(document)

store(docs,namespace="NITKKR")








