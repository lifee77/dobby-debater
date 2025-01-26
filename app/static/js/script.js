// DOM Elements
const debateModeBtn = document.getElementById('debate-mode-btn');
const instructorModeBtn = document.getElementById('instructor-mode-btn');
const modeIndicator = document.getElementById('mode-indicator');
const debateForm = document.getElementById('debate-form');
const responseSection = document.getElementById('response-section');
const responseText = document.getElementById('response-text');
const topicDropdown = document.getElementById('topic');
const manualTopicContainer = document.getElementById('manual-topic-container');
const manualTopicInput = document.getElementById('manual-topic');

// Variables
let mode = '';

// Update the mode indicator text
function updateModeIndicator(selectedMode) {
    modeIndicator.innerHTML = `<p>Selected Mode: <strong>${selectedMode}</strong></p>`;
}

// Highlight the active button
function activateButton(button) {
    debateModeBtn.classList.remove('active');
    instructorModeBtn.classList.remove('active');
    button.classList.add('active');
}

// Handle Debate Mode Button Click
debateModeBtn.addEventListener('click', () => {
    mode = 'debate';
    debateForm.style.display = 'block';
    responseSection.style.display = 'none';
    activateButton(debateModeBtn);
    updateModeIndicator('Debate Mode');
});

// Handle Instructor Mode Button Click
instructorModeBtn.addEventListener('click', () => {
    mode = 'instructor';
    debateForm.style.display = 'block';
    responseSection.style.display = 'none';
    activateButton(instructorModeBtn);
    updateModeIndicator('Instructor Mode');
});

// Show or hide the manual topic input based on dropdown selection
topicDropdown.addEventListener('change', () => {
    if (topicDropdown.value === 'manual') {
        manualTopicContainer.style.display = 'block';
    } else {
        manualTopicContainer.style.display = 'none';
    }
});

// Handle Form Submission
debateForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Determine the topic: use manual input if selected
    let topic = topicDropdown.value;
    if (topic === 'manual') {
        topic = manualTopicInput.value.trim();
        if (!topic) {
            responseText.innerHTML = "Please enter a custom topic.";
            responseSection.style.display = 'block';
            return;
        }
    }

    // Collect other form data
    const userInput = document.getElementById('user-input').value.trim();
    const model = document.getElementById('model').value;

    if (!userInput) {
        responseText.innerHTML = "Please enter your argument.";
        responseSection.style.display = 'block';
        return;
    }

    // Display loading text
    responseText.innerHTML = mode === 'debate' ? "Dobby is preparing a response..." : "Dobby is analyzing your argument...";
    responseSection.style.display = 'block';

    try {
        // Send the request to the backend
        const res = await fetch(`/${mode}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_input: userInput, topic: topic, model: model }),
        });

        // Handle the response
        if (!res.ok) {
            throw new Error("Failed to fetch response. Please try again.");
        }

        const data = await res.json();
        responseText.innerHTML = `<span class="rendered-text">${mode === 'debate' ? data.response : data.feedback}</span>`;
    } catch (err) {
        // Handle errors
        responseText.innerHTML = "Error: " + err.message;
    }
});