import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to ask Gemini LLM
def ask_llm(prompt: str, system: str = "You are a smart planning agent") -> str:
    """
    Sends a prompt to Gemini LLM with an optional system message.
    Returns the model's response as a string.
    """
    try:
        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat(history=[])

        full_prompt = f"{system.strip()}\n\n{prompt.strip()}"
        response = chat.send_message(full_prompt)

        return response.text.strip()

    except Exception as e:
        return f"❌ Error communicating with Gemini: {e}"

