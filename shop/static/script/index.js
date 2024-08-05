const cartbtns = document.querySelectorAll(".cart");

function update(cart) {
  for (var item in cart) {
    var id = item.split("pr")[1];
    document.getElementById(`div${id}`).innerHTML = `
    <button id="minus${id}" class="btn btn-light minus">
      -
    </button>
    <p class="text-light qyt">${cart[`pr${id}`]}</p>  
    <button id="plus${id}" class="btn btn-light plus">
      +
    </button>
    `;
  }
}

let cart = {};

if (localStorage.getItem("cart")) {
  cart = JSON.parse(localStorage.getItem("cart"));
  update(cart);
}

cartbtns.forEach((cartbtn) => {
  cartbtn.addEventListener("click", () => {
    var id = cartbtn.id;
    if (cart[id]) {
      cart[id] = cart[id] + 1;
    } else {
      cart[id] = 1;
    }
    update(cart);
    minuses = document.querySelectorAll(".minus");
    pluses = document.querySelectorAll(".plus");
    cartLink.innerText = `(${Object.keys(cart).length})`;
    localStorage.setItem("cart", JSON.stringify(cart));
    window.location.replace("http://localhost:8000/shop/")
  });
});

  let minuses = document.querySelectorAll(".minus");
  minuses.forEach((minus) => {
    minus.addEventListener("click", () => {
      var prid = minus.id.split("minus")[1];
      cart[`pr${prid}`] = cart[`pr${prid}`] - 1;
      cart[`pr${prid}`] = Math.max(0, cart[`pr${prid}`]);
      document.querySelector(`#div${prid} p`).innerText = cart[`pr${prid}`];
      localStorage.setItem("cart", JSON.stringify(cart));
    });
  });

  let pluses = document.querySelectorAll(".plus");

  pluses.forEach((plus) => {
    plus.addEventListener("click", () => {
      var prid = plus.id.split("plus")[1];
      cart[`pr${prid}`] = cart[`pr${prid}`] + 1;
      document.querySelector(`#div${prid} p`).innerText = cart[`pr${prid}`];
      localStorage.setItem("cart", JSON.stringify(cart));
    });
  });

