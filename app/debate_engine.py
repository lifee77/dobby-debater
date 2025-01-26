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

def generate_response(user_input, topic, model):
    """
    Generates a debate response from the selected Dobby model as an opponent.
    """
    try:
        payload = {
            "model": model,
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

def generate_feedback(user_input, topic, model):
    """
    Provides constructive feedback on the user's debate argument.
    """
    try:
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": (
                        f"You are a skilled debate instructor helping a student improve their argumentation skills. "
                        f"Critically evaluate the student's argument on the topic '{topic}' and provide specific, actionable feedback. "
                        f"Identify the strengths of their argument, point out weaknesses, and suggest ways to strengthen their reasoning, evidence, and delivery:\n\n"
                        f"User's Argument: {user_input}\n\nInstructor Feedback:"
                    ),
                }
            ],
            "max_tokens": 300,
        }
        response = requests.post(BASE_URL, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    except Exception as e:
        return f"Error: {str(e)}"
