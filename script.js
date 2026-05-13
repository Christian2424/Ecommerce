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



