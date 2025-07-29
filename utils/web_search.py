import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def search_web(query):
    try:
        prompt = f"""
        You are a helpful AI assistant with access to the web. The user has searched: \"{query}\".
        First provide one pinpoint answer in a paragraph and then simulate a web search by returning 3 relevant links with a title and snippet each.

        Output format:
        [
            {{"title": "...", "link": "...", "snippet": "..."}},
            ...
        ]
        """

        response = model.generate_content(prompt)
        output = response.text

        # Parse simple JSON-like structure manually
        import re, json
        try:
            json_like = re.search(r'\[.*\]', output, re.DOTALL)
            if json_like:
                return json.loads(json_like.group())
        except Exception:
            return []

    except Exception as e:
        print("Error in Gemini web search:", e)
        return []
