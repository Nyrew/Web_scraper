fetch('http://127.0.0.1:5000/products')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.getElementById('product-table');
        data.forEach(product => {
            const row = document.createElement('tr');
            row.innerHTML = `<td>${product.name}</td><td>${product.price}</td>`;
            tableBody.appendChild(row);
        });
    })
    .catch(error => console.error('Error fetching data:', error));
