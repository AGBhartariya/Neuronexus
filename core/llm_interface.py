# core/llm_interface.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_llm(prompt, system="You are a helpful assistant. Solve the problem to its full extent."):
    model = genai.GenerativeModel("gemini-2.0-flash")
    full_prompt = f"{system}\n\n{prompt}"
    response = model.generate_content(full_prompt)
    return response.text.strip()
