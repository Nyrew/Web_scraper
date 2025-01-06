const scrapeButton = document.getElementById("scrape-button");
const alzaGrid = document.querySelector("#alza .card-grid");
const istyleGrid = document.querySelector("#istyle .card-grid");
const backendUrl = process.env.BACKEND_URL

scrapeButton.addEventListener("click", async () => {
    try {
        
        // Zavolej backend pro scraping
        await fetch(`${backendUrl}/scrape`, {
            method: "POST",
        });
        // Fetch data from backend
        const response = await fetch(`${backendUrl}/products`);
        const result = await response.json();

        if (result.status === "success") {
            const data = result.data;

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
        } else {
            alert("Error fetching products: " + result.message);
        }
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