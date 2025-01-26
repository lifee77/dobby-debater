const debateModeBtn = document.getElementById('debate-mode-btn');
const instructorModeBtn = document.getElementById('instructor-mode-btn');
const debateForm = document.getElementById('debate-form');
const responseSection = document.getElementById('response-section');
const responseText = document.getElementById('response-text');

let mode = '';

debateModeBtn.addEventListener('click', () => {
    mode = 'debate';
    debateForm.style.display = 'block';
    responseSection.style.display = 'none';
});

instructorModeBtn.addEventListener('click', () => {
    mode = 'instructor';
    debateForm.style.display = 'block';
    responseSection.style.display = 'none';
});

debateForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const userInput = document.getElementById('user-input').value;
    const topic = document.getElementById('topic').value;
    responseText.textContent = mode === 'debate' ? "Dobby is preparing a response..." : "Dobby is analyzing your argument...";

    try {
        const res = await fetch(`/${mode}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_input: userInput, topic: topic }),
        });

        const data = await res.json();
        responseText.textContent = mode === 'debate' ? data.response : data.feedback;
        responseSection.style.display = 'block';
    } catch (err) {
        responseText.textContent = "Something went wrong! Please try again later.";
        responseSection.style.display = 'block';
    }
});
