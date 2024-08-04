const cartbtns = document.querySelectorAll(".cart");

let cart = {};

if (localStorage.getItem("cart")) {
  cart = JSON.parse(localStorage.getItem("cart"));
}

for (let i = 0; i < cartbtns.length; i++) {
  if (cart[`pr${i}`]) {
    var text = document.getElementById(`text${i}`);
    text.innerText = `In cart: ${cart[`pr${i}`]}`;
  }
}

cartbtns.forEach((cartbtn) => {
  cartbtn.addEventListener("click", () => {
    var id = cartbtn.id;
    var textId = id.split("pr");
    var text = document.getElementById(`text${textId[1]}`);
    if (cart[id]) {
      cart[id] = cart[id] + 1;
    } else {
      cart[id] = 1;
    }

    text.innerText = `In cart: ${cart[id]}`;
    cartLink.innerText = `(${Object.keys(cart).length})`;
    localStorage.setItem("cart", JSON.stringify(cart));

  });
});
