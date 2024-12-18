from pinecone import Pinecone
import google.generativeai as genai


genai.configure(api_key="AIzaSyCqS4dnLO_qKB4aqrh3VZPh1wfEOyUN75E")
pc = Pinecone(api_key="178bd010-c7d2-4a89-ab96-d3813eff6792")
index = pc.Index("mogga")


def clean_vector_id(vector_id):
    vector_id = ''.join(char for char in vector_id if ord(char) < 128)
    return vector_id



def generate_embeddings(text):
    result = genai.embed_content(
    model="models/text-embedding-004", 
    content=text,
    task_type="retrieval_document")
    embeddings = result['embedding']
    return embeddings


