// Function to generate a random excuse
async function generateExcuse() {
    const categorySelect = document.getElementById("categorySelect");
    const excuseDisplay = document.getElementById("excuseDisplay");
    const generateButton = document.getElementById("generateButton");

    // Get the selected category
    const selectedCategory = categorySelect.value;

    // Disable button and show loading state
    generateButton.disabled = true;
    excuseDisplay.textContent = "Generating excuse...";

    try {
        const response = await fetch("http://127.0.0.1:5000/generate-excuse", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                category: selectedCategory
            })
        });

        const data = await response.json();
        
        if (response.ok && data.excuse) {
            excuseDisplay.textContent = data.excuse;
        } else {
            excuseDisplay.textContent = data.error || "Failed to generate excuse. Please try again!";
        }
    } catch (error) {
        console.error("Error generating excuse:", error);
        excuseDisplay.textContent = "Oops! Something went wrong. Try again later.";
    } finally {
        // Re-enable button
        generateButton.disabled = false;
    }
}

// Add click handler to the generate button
document.addEventListener('DOMContentLoaded', function() {
    const generateButton = document.getElementById("generateButton");
    if (generateButton) {
        generateButton.addEventListener("click", generateExcuse);
    } else {
        console.error("Generate button not found!");
    }
});