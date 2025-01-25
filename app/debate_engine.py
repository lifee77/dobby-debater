import requests
import os

API_KEY = os.getenv("API_KEY")

def generate_response(user_input, topic):
    """
    Generates a response from the Dobby API based on user input and topic.
    """
    try:
        # Call the Fireworks API with Dobby
        response = requests.post(
            "https://api.fireworks.ai/v1/generate",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={
                "model": "Dobby-Mini-Leashed-Llama-3.1-8B",
                "prompt": f"Topic: {topic}\nUser: {user_input}\nDobby:",
                "max_tokens": 200,
            },
        )
        if response.status_code == 200:
            return response.json().get("text", "Dobby has nothing to say!")
        else:
            return "Dobby is experiencing a hiccup. Please try again."
    except Exception as e:
        return f"Error: {str(e)}"
