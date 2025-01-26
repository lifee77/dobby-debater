const debateModeBtn = document.getElementById('debate-mode-btn');
const instructorModeBtn = document.getElementById('instructor-mode-btn');
const modeIndicator = document.getElementById('mode-indicator');
const debateForm = document.getElementById('debate-form');
const responseSection = document.getElementById('response-section');
const responseText = document.getElementById('response-text');

let mode = '';

function updateModeIndicator(selectedMode) {
    modeIndicator.innerHTML = `<p>Selected Mode: <strong>${selectedMode}</strong></p>`;
}

function activateButton(button) {
    debateModeBtn.classList.remove('active');
    instructorModeBtn.classList.remove('active');
    button.classList.add('active');
}

debateModeBtn.addEventListener('click', () => {
    mode = 'debate';
    debateForm.style.display = 'block';
    responseSection.style.display = 'none';
    activateButton(debateModeBtn);
    updateModeIndicator('Debate Mode');
});

instructorModeBtn.addEventListener('click', () => {
    mode = 'instructor';
    debateForm.style.display = 'block';
    responseSection.style.display = 'none';
    activateButton(instructorModeBtn);
    updateModeIndicator('Instructor Mode');
});

debateForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const userInput = document.getElementById('user-input').value;
    const topic = document.getElementById('topic').value;
    const model = document.getElementById('model').value;

    responseText.textContent = mode === 'debate' ? "Dobby is preparing a response..." : "Dobby is analyzing your argument...";

    try {
        const res = await fetch(`/${mode}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_input: userInput, topic: topic, model: model }),
        });

        const data = await res.json();
        responseText.textContent = mode === 'debate' ? data.response : data.feedback;
        responseSection.style.display = 'block';
    } catch (err) {
        responseText.textContent = "Something went wrong! Please try again later.";
        responseSection.style.display = 'block';
    }
});
