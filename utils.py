import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def config_gemeni():
    return genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_text(client, prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
