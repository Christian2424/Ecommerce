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
    const response = await fetch('http://127.0.0.1:5000/getbestseller');
    const data = await response.json();
    container_bestseller = document.getElementById('container_card_bestseller')
    data.forEach(product => {
    container_card = document.createElement('div');
    container_card.innerHTML =  `
    <div class="card" style="width: 18rem;">
        <img src="${product.img_url}" class="card-img-top" alt="...">
        <div class="card-body">
            <h3> ${product.name} </h3>
            <p class="card-text">${product.price}</p>
        </div>
    </div>
    `;
    container_bestseller.appendChild(container_card)
    });

}

caricaBestseller()
