# Dobby Debater

Dobby Debater is an interactive AI-powered debate bot built using the Dobby API. This project aims to create a bold and unfiltered conversational AI capable of debating philosophical, societal, or personal topics with users.

## Features

- Dynamic debate topics (philosophy, technology, ethics, etc.)
- Blunt and witty responses
- Adjustable tone and difficulty
- Real-time interactive UI

## How It Works

1. The user selects a topic or inputs their own.
2. Dobby generates an argument based on the chosen topic.
3. The user responds, and Dobby continues the debate in real time.

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript (for dynamic UI)
- **AI Model**: Dobby-Mini-Leashed-Llama-3.1-8B via the Fireworks API
- **Testing**: Pytest

## Getting Started

### Prerequisites

- Python 3.11
- Virtual environment tools (`venv` or `conda`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lifee77/dobby-debater
   cd dobby-debator

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your `.env` file:
    ```env
    API_KEY=your_fireworks_api_key
    ```

### Running the App

1. Start the Flask server:
    ```bash
    python app/main.py
    ```

2. Open your browser and go to:
    ```arduino
    http://127.0.0.1:5000
    ```

### File Descriptions
```
DobbyDebater/
├── README.md
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── debate_engine.py
│   └── responses.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── debate.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
├── tests/
│   ├── test_debate_engine.py
│   └── test_responses.py
└── .env
```


- `main.py`: Entry point for the Flask app.
- `debate_engine.py`: Core logic for generating debate arguments.
- `responses.py`: Helper functions for handling and formatting responses.
- `templates/`: HTML templates for the app.
- `static/`: CSS and JavaScript files for UI styling and interaction.
- `tests/`: Unit tests for the backend.

### Example Usage

1. Start the app and open the home page.
2. Select a topic (e.g., "Freedom of Speech") or type your own.
3. Engage in a debate with Dobby.
4. Adjust the tone or style mid-debate for a dynamic experience.

### Future Enhancements

- Add multiplayer mode for group debates.
- Implement voice-to-text and text-to-voice features.
- Introduce a scoring system to rate user and Dobby's debate points.

### License

This project is licensed under the MIT License. See `LICENSE` for more details.
