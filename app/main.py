from flask import Flask, render_template, request, jsonify
from debate_engine import generate_response, generate_feedback
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/debate', methods=['POST'])
def debate():
    user_input = request.json.get('user_input')
    topic = request.json.get('topic')
    model = request.json.get('model')
    response = generate_response(user_input, topic, model)
    return jsonify({'response': response})

@app.route('/instructor', methods=['POST'])
def instructor():
    user_input = request.json.get('user_input')
    topic = request.json.get('topic')
    model = request.json.get('model')
    feedback = generate_feedback(user_input, topic, model)
    return jsonify({'feedback': feedback})


if __name__ == '__main__':
    app.run(debug=True)
