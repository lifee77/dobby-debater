# Dobby Debater

Dobby Debater is an interactive AI-powered debate platform leveraging the **Dobby API**. The app allows users to engage in debates with a bold, witty AI and even receive constructive feedback from a debate instructor. Dobby is designed to champion liberty and cryptocurrency, ensuring spirited debates on a range of topics.

---

## Features

### Core Functionality:
- **Debate Mode**: Engage with Dobby as your debate opponent on various philosophical, societal, and technological topics.
- **Instructor Mode**: Receive personalized feedback from Dobby to improve your debating skills.
  
### Dynamic Topics:
- Predefined topics (e.g., Freedom of Speech, Cryptocurrency, Ethics in Technology).
- Option to add your custom topic dynamically.

### Models:
- Two models available for selection:
  - **Dobby Leashed**: Balanced and polite.
  - **Dobby Unhinged**: Bold, unfiltered, and provocative.

### Real-Time Interactive UI:
- Responsive design for all devices.
- Text formatting for Dobby’s output (e.g., bold, italic).
- Mode selection with clear visual indicators.

---

### **How It Works**

1. **Select a mode:**
   - **Debate Mode**: Engage with Dobby as your debate opponent.
   - **Instructor Mode**: Receive personalized feedback to improve your debating skills.

2. **Choose a model type:**
   - **Dobby Leashed**: Polite and balanced responses.
   - **Dobby Unhinged**: Bold, provocative, and unfiltered responses.

3. **Pick a topic:**
   - Select from predefined topics (e.g., "Freedom of Speech", "Cryptocurrency").
   - Add a custom topic if desired.

4. **Submit your argument:**
   - Dobby responds in real-time based on the selected mode and model.
   - Responses are formatted with rich text (e.g., bold, italic) for better readability.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript (dynamic UI)
- **AI Integration**: Dobby API via Fireworks
- **Deployment**: Compatible with platforms like Heroku, Render, or Docker
- **Testing**: Pytest

---

## Getting Started

### Prerequisites

- Python 3.11+
- Virtual environment tools (`venv` or `conda`)

---

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/lifee77/dobby-debater
    cd dobby-debater
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your `.env` file:
    ```env
    FIREWORKS_API_KEY=your_fireworks_api_key
    ```

---

### Running the App

1. Start the Flask server:
    ```bash
    python app/main.py
    ```

2. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```

---

### File Structure

```plaintext
DobbyDebater/
├── README.md
├── app/
│   ├── __init__.py
│   ├── main.py              # Entry point for the Flask app
│   ├── debate_engine.py     # Core logic for Dobby's arguments
│   └── responses.py         # Helper functions for formatting responses
├── requirements.txt         # Python dependencies
├── templates/               # HTML templates
│   └── home.html
├── static/                  # CSS and JavaScript for UI
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
├── tests/                   # Unit tests for backend logic
│   ├── test_debate_engine.py
│   └── test_responses.py
└── .env                     # Environment variables (API keys, etc.)
```

---

### Example Usage

1. Launch the app and visit the homepage.
2. Select a mode:
   - **Debate Mode**: Engage Dobby in an argument on a chosen topic.
   - **Instructor Mode**: Receive constructive feedback on your debating skills.
3. Choose a predefined topic or add a custom one.
4. View Dobby's formatted response in real time.

---

### Deployment Options

This app is ready to be deployed on multiple platforms:
- **Heroku**: Follow the Heroku deployment guide for Flask apps.
- **Render**: Use Render’s simple deployment for Python applications.
- **Docker**: Build a Docker image for scalability.

---

### Future Enhancements

- **Multiplayer Mode**: Allow multiple users to join and debate Dobby or each other.
- **Voice Features**: Implement text-to-speech and speech-to-text for voice-based debates.
- **Scoring System**: Add a scoring mechanism to rate debate points for both the user and Dobby.
- **Advanced Analytics**: Track user improvement in instructor mode.

---

### License

This project is licensed under the MIT License. See `LICENSE` for more details.
