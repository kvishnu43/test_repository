from google import genai
import os  # type: ignore

# The client automatically looks for an environment variable named GEMINI_API_KEY
client = genai.Client(api_key='API_KEY')

try:
    response = client.models.generate_content(  # type: ignore
        model="gemini-2.0-flash",
        contents="Are you active?"
    )
    print("Success:", response.text)
except Exception as e:
    print(f"Failed again: {e}")



