import pytest
from app.debate_engine import generate_response

def test_generate_response():
    # Mock API key and inputs
    mock_input = "Why is freedom important?"
    mock_topic = "Freedom of Speech"
    response = generate_response(mock_input, mock_topic)
    assert isinstance(response, str), "Response should be a string."
