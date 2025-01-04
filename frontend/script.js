const scrapeButton = document.getElementById("scrape-button");
const alzaGrid = document.querySelector("#alza .card-grid");
const istyleGrid = document.querySelector("#istyle .card-grid");

scrapeButton.addEventListener("click", async () => {
    try {
        // Fetch data from backend
        const response = await fetch("https://your-backend-url.onrender.com/scrape");
        const data = await response.json();

        // Clear existing cards
        alzaGrid.innerHTML = "";
        istyleGrid.innerHTML = "";

        // Populate Alza cards
        data.alza.forEach((product) => {
            const card = createCard(product);
            alzaGrid.appendChild(card);
        });

        // Populate Istyle cards
        data.istyle.forEach((product) => {
            const card = createCard(product);
            istyleGrid.appendChild(card);
        });
    } catch (error) {
        console.error("Error fetching data:", error);
        alert("Failed to fetch data. Please try again later.");
    }
});

// Helper function to create a card element
function createCard(product) {
    const card = document.createElement("div");
    card.classList.add("card");

    card.innerHTML = `
        <h3>${product.name}</h3>
        <p>RAM: ${product.ram}</p>
        <p>SSD: ${product.ssd}</p>
        <p>Price: ${product.price}</p>
    `;

    return card;
}
