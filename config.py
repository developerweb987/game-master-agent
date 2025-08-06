import os
from google.generativeai import configure, GenerativeModel

def get_gemini_api_key():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("API Key not found in .env")
    return api_key

def get_gemini_model():
    api_key = get_gemini_api_key()
    configure(api_key=api_key)
    return GenerativeModel("gemini-2.0-flash")
