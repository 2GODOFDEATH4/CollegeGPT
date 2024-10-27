from pinecone import Pinecone
import google.generativeai as genai
import random
import hashlib
from utils import chunk_json

genai.configure(api_key="AIzaSyCqS4dnLO_qKB4aqrh3VZPh1wfEOyUN75E")
pc = Pinecone(api_key="178bd010-c7d2-4a89-ab96-d3813eff6792")
index = 'nitkkrbot'


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
        

def store(text, namespace):
    index = pc.Index("nitkkrbot")
    vectors = []
    
    for i in text:
        clean_text = clean_vector_id(str(i))
        unique_id = hashlib.md5(clean_text.encode('utf-8')).hexdigest()
        vectors.append({
            "id": unique_id,
            "values": generate_embeddings(text=clean_text),
            "metadata": {
                'text': clean_text
            }
        })
    index.upsert(vectors=vectors, namespace=namespace)
    print('Embedding Generation and Data Storage Done')


def similarity(question, namespace, top_k=3):
    question_embedding = generate_embeddings(question)
    index = pc.Index("nitkkrbot")

    # Query the index
    response = index.query(
        vector=question_embedding,
        top_k=top_k,
        namespace=namespace,
        include_metadata=True
    )

    pokemon = ''

    for i in response.matches :
        pokemon += i.metadata['text']
    
    return pokemon


def store_json(student_data, namespace="NITKKR", batch_size=10):
    index = pc.Index("nitkkrbot")
    vectors = []
    
    # Process in batches
    for i in range(0, len(student_data), batch_size):
        batch = student_data[i:i+batch_size]
        for chunk in batch:
            clean_text = clean_vector_id(chunk['chunk_text'])
            unique_id = hashlib.md5(clean_text.encode('utf-8')).hexdigest()

            # Create vector for Pinecone
            vectors.append({
                "id": unique_id,
                "values": generate_embeddings(clean_text),
                "metadata": chunk['metadata']
            })

        # Upsert batch to Pinecone
        index.upsert(vectors=vectors, namespace=namespace)
        print(f"Batch {i // batch_size + 1} upserted")

    print('Embedding Generation and Data Storage Done')



