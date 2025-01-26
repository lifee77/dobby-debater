import requests
import os

API_KEY = os.getenv("API_KEY")

def generate_response(user_input, topic):
    """
    Generates a debate response from Dobby as an opponent.
    """
    try:
        response = requests.post(
            "https://api.fireworks.ai/v1/generate",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={
                "model": "Dobby-Mini-Leashed-Llama-3.1-8B",
                "prompt": f"You are an expert debater. The topic is '{topic}'. Respond to the user's argument as their debate opponent:\n\nUser: {user_input}\nDobby:",
                "max_tokens": 200,
            },
        )
        if response.status_code == 200:
            return response.json().get("text", "Dobby has nothing to say!")
        else:
            return "Dobby is experiencing a hiccup. Please try again."
    except Exception as e:
        return f"Error: {str(e)}"

def generate_feedback(user_input, topic):
    """
    Provides constructive feedback on the user's debate argument.
    """
    try:
        response = requests.post(
            "https://api.fireworks.ai/v1/generate",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={
                "model": "Dobby-Mini-Leashed-Llama-3.1-8B",
                "prompt": f"You are a debate instructor helping a student improve their argumentation skills. The topic is '{topic}'. Analyze the user's argument and provide constructive feedback:\n\nUser's Argument: {user_input}\nInstructor Feedback:",
                "max_tokens": 200,
            },
        )
        if response.status_code == 200:
            return response.json().get("text", "Dobby has no feedback to offer!")
        else:
            return "Dobby is experiencing a hiccup. Please try again."
    except Exception as e:
        return f"Error: {str(e)}"
