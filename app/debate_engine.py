import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Load the Fireworks API key from the environment
API_KEY = os.getenv("FIREWORKS_API_KEY")
BASE_URL = "https://api.fireworks.ai/inference/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

def generate_response(user_input, topic):
    """
    Generates a debate response from Dobby as an opponent.
    """
    try:
        payload = {
            "model": "accounts/sentientfoundation/models/dobby-mini-unhinged-llama-3-1-8b#accounts/sentientfoundation/deployments/81e155fc",
            "messages": [
                {
                    "role": "user",
                    "content": f"Topic: {topic}\nUser: {user_input}\nDobby:",
                }
            ],
            "max_tokens": 200,
        }
        response = requests.post(BASE_URL, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    except Exception as e:
        return f"Error: {str(e)}"

def generate_feedback(user_input, topic):
    """
    Provides constructive feedback on the user's debate argument.
    """
    try:
        payload = {
            "model": "accounts/sentientfoundation/models/dobby-mini-unhinged-llama-3-1-8b#accounts/sentientfoundation/deployments/81e155fc",
            "messages": [
                {
                    "role": "user",
                    "content": f"You are a debate instructor helping a student improve their argumentation skills. The topic is '{topic}'. Analyze the user's argument and provide constructive feedback:\n\nUser's Argument: {user_input}\nInstructor Feedback:",
                }
            ],
            "max_tokens": 200,
        }
        response = requests.post(BASE_URL, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    except Exception as e:
        return f"Error: {str(e)}"
