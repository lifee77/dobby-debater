document.getElementById('debate-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const userInput = document.getElementById('user-input').value;
    const topic = document.getElementById('topic').value;

    const responseSection = document.getElementById('response-section');
    const responseText = document.getElementById('response-text');

    responseText.textContent = "Dobby is thinking...";

    try {
        const res = await fetch('/debate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_input: userInput, topic: topic }),
        });

        const data = await res.json();
        responseText.textContent = data.response;
    } catch (err) {
        responseText.textContent = "Something went wrong! Try again later.";
    }
});
