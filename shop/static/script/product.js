const span = document.querySelectorAll("span");
const main = document.getElementById("main");

let id = span[3].id.split("qyt")[1];

let cart = {};
if (localStorage.getItem("cart")) {
  cart = JSON.parse(localStorage.getItem("cart"));
}

if (cart[`pr${id}`]) {
  main.innerHTML = `<div class="d-flex div-main">
            <div class="d-flex align-items-center div-qyt">
              <button type="btn" class="btn btn-light prd-min">-</button>
              <p class="text-light">${cart[`pr${id}`]}</p>
              <button type="btn" class="btn btn-light prd-pls">+</button>
            </div>
            <div class="div-gocart">
              <a href="http://localhost:8000/shop/cart" class="btn btn-light">Go to cart</a>
            </div>
          </div>`;
}

const prdMin = document.querySelector(".prd-min");
const prdPls = document.querySelector(".prd-pls");

if(prdMin && prdPls){
  prdMin.addEventListener("click",() => {
    cart[`pr${id}`] = cart[`pr${id}`] - 1;
    cart[`pr${id}`] = Math.max(0, cart[`pr${id}`])
    document.querySelector(".div-qyt p").innerText = cart[`pr${id}`]
    localStorage.setItem("cart", JSON.stringify(cart));
  });
  prdPls.addEventListener("click", () => {
    cart[`pr${id}`] = cart[`pr${id}`] + 1;
    document.querySelector(".div-qyt p").innerText = cart[`pr${id}`];
    localStorage.setItem("cart", JSON.stringify(cart));
  })
}

const crtBtn = document.getElementById(`crt${id}`);
if (crtBtn) {
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
    window.location.replace(`http://localhost:8000/shop/product/${id}`)
  });
}
