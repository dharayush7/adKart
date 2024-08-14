let cartLink = document.getElementById("cartLink");
let pop = document.getElementById("pop");
let body = document.querySelector(".popover-body");

cart = localStorage.getItem("cart");

if (cart) {
  jsonCart = JSON.parse(cart);
  cartLink.innerHTML = `(${Object.keys(jsonCart).length})`;
}

const height = window.innerHeight;
const mainHeight = height - 180;

document.querySelector("main").style = `min-height: ${mainHeight}px`;
