const span = document.querySelectorAll("span");

let id = span[3].id.split("qyt")[1];

let cart = {};
if (localStorage.getItem("cart")) {
  cart = JSON.parse(localStorage.getItem("cart"));
}

if (cart[`pr${id}`]) {
  span[3].innerText = cart[`pr${id}`];
}

const crtBtn = document.getElementById(`crt${id}`);

crtBtn.addEventListener("click", () => {
  console.log("clicked");
  if (cart[`pr${id}`]) {
    cart[`pr${id}`] = cart[`pr${id}`] + 1;
  } else {
    cart[`pr${id}`] = 1;
  }
  span[3].innerText = cart[`pr${id}`];
  cartLink.innerText = `(${Object.keys(cart).length})`;
  localStorage.setItem("cart", JSON.stringify(cart));
});
