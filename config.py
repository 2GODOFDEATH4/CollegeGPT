import os
from dotenv import load_dotenv
try:
    import streamlit as st
except ImportError:
    st = None

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

if st is not None:
    GEMINI_API_KEY = GEMINI_API_KEY or st.secrets.get("GEMINI_API_KEY")
    PINECONE_API_KEY = PINECONE_API_KEY or st.secrets.get("PINECONE_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("Missing required environment variable: GEMINI_API_KEY")

if not PINECONE_API_KEY:
    raise RuntimeError("Missing required environment variable: PINECONE_API_KEY")
