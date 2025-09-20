document.getElementById("generateBtn").addEventListener("click", async () => {
    const data = document.getElementById("dataInput").value.trim();
    if (!data) return alert("Please enter some text or URL!");

    const response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data })
    });

    if (!response.ok) {
        alert("Error generating QR code.");
        return;
    }

    const result = await response.json();
    const qrContainer = document.getElementById("qrContainer");
    qrContainer.innerHTML = `<h2>Your QR Code:</h2><img src="data:image/png;base64,${result.qr_code}" alt="QR Code">`;
});
