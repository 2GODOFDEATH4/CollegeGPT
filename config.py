import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("Missing required environment variable: GEMINI_API_KEY")

if not PINECONE_API_KEY:
    raise RuntimeError("Missing required environment variable: PINECONE_API_KEY")
