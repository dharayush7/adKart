let cartLink = document.getElementById("cartLink");
let pop = document.getElementById("pop")
let body = document.querySelector('.popover-body')

cart = localStorage.getItem('cart')

if(cart){
    jsonCart = JSON.parse(cart);
    cartLink.innerHTML = `(${Object.keys(jsonCart).length})`
}






