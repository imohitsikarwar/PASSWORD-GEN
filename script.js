function generatePassword() {
    let length = document.getElementById("length").value;
    // /fetch(`/generate?length=${length}`)
    fetch(`http://127.0.0.1:5000/generate?length=${length}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("generatedPassword").value = data.password;
        });
}

function analyzePassword() {
    let password = document.getElementById("passwordInput").value;
    fetch('http://127.0.0.1:5000/analyze', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ password })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("strengthResult").innerText = `Strength: ${data.strength} (Entropy: ${data.entropy})`;

        });
}