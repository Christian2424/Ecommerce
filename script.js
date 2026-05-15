img_search = document.getElementById("search_icon")
box_search = document.querySelector(".search_box")

img_search.addEventListener("click", () =>{
    box_search.classList.toggle("active")
})


img_login = document.getElementById("login_icon")
box_login = document.querySelector(".login_box")

img_login.addEventListener("click", () =>{
    box_login.classList.toggle("active")
})


cart_bar = document.getElementById("offcanvas")
cart_icon = document.getElementById("cart_icon")

cart_icon.addEventListener("click", () =>{
    cart_bar.classList.toggle("show")
})

async function caricaBestseller() {
    // 1. Chiamiamo la rotta che hai creato
    const response = await fetch('/getbestseller');
    const data = await response.json();
    document.appendChild(document.createElement('div')).textContent = JSON.stringify(data);
    // 2. Creiamo dinamicamente gli elementi HTML per mostrare i bestseller
    const bestsellerContainer = document.getElementById('bestseller-container');
    data.forEach(product => {
        const productCard = document.createElement('div');
        productCard.classList.add('product-card');
        productCard.innerHTML = `
            <img src="${product.image_url}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>Price: $${product.price}</p>
        `;
        bestsellerContainer.appendChild(productCard);
    });
}

