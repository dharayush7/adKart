const container = document.getElementById("container");

const csrf = document.querySelector("#csrf input").value;

let cart = {};
if (localStorage.getItem("cart")) {
  cart = JSON.parse(localStorage.getItem("cart"));
  if (Object.keys(cart).length == 0) {
    container.innerHTML = `<div class="container d-flex cart-card mb-4">
            <div class="container mt-2 justify-content-center">
                <p class="fs-1 text-light" style="text-align: center;">Your Cart Is Empty...</p>
            </div>
        </div>`;
  } else {
    render(cart);
    checkOut(cart);
  }
} else {
  container.innerHTML = `<div class="container d-flex cart-card mb-4">
            <div class="container mt-2 justify-content-center">
                <p class="fs-1 text-light" style="text-align: center;">Your Cart Is Empty...</p>
            </div>
        </div>`;
}

async function checkOut(cart) {
  let p = 0;
  let keys = Object.keys(cart);
  keys.forEach(async (key) => {
    let data = await get(key);
    let qyt = 0 + cart[key];
    let pr = 0 + data.price;
    p = p + qyt * pr;
    let st = "";
    if (p == 0) {
      st = "disabled";
    }
    document.getElementById("out").innerHTML = `
    <div class="d-flex justify-content-end align-items-end flex-column">
      <div class="">
        <p class="text-light text-center fs-3">Total: $ ${p}.00</p>
      </div>
      <div>
        <button type="button" class="btn btn-danger" style="margin-right: 10px;" id="clcr">Clear Cart</button>
        <button type="button" class="btn btn-light" style="margin-left: 10px;" id="chot" ${st}>Checkout</button>
        
      </div>
    </div>
    `;
    document.getElementById("clcr").addEventListener("click", () => {
      localStorage.removeItem("cart");
      window.location.replace("http://localhost:8000/shop/cart");
    });
    document.getElementById("chot").addEventListener("click", () => {
      window.location.replace("http://localhost:8000/shop/checkout");
    });
  });
}

async function render(cart) {
  let p = "";
  let keys = Object.keys(cart);
  keys.forEach(async (key) => {
    let data = await get(key);
    let p1 = `
    <div class="container d-flex cart-card mb-4">
            <div>
                <img class="prd-image" src="/media/${await data.image}" alt="">
            </div>
            <div class="div-name" >
                <p class="text-light prd-name">${await data.product_name}</p>
            </div>
            <div >
                <p class="text-light prd-name">$ ${await data.price}.00</p>
            </div>
            <div class="d-flex align-items-center">
                <div class="prd-qyt">
                <p class="text-light">Qyt:</p>
                </div>
                <button class="btn btn-light btn-minus" id="mn${key}">-</button>
                <p class="text-light prd-qyt-no" id="qyt${key}">${cart[key]}</p>
                <button class="btn btn-light btn-plus" id="pl${key}">+</button>
            </div>
            <div>
                <button class="btn btn-danger del" id="del${key}">Delete</button>
            </div>
    </div>
    `;
    p = p + p1;
    container.innerHTML = p;

    const btnMinuses = document.querySelectorAll(".btn-minus");
    const btnPluses = document.querySelectorAll(".btn-plus");
    const btndels = document.querySelectorAll(".del");

    btnMinuses.forEach((btnMinus) => {
      btnMinus.addEventListener("click", () => {
        let btnid = btnMinus.id.split("mn")[1];
        cart[btnid] = cart[btnid] - 1;
        cart[btnid] = Math.max(0, cart[btnid]);
        document.getElementById(`qyt${btnid}`).innerText = cart[btnid];
        checkOut(cart);
        localStorage.setItem("cart", JSON.stringify(cart));
      });
    });

    btnPluses.forEach((btnPlus) => {
      btnPlus.addEventListener("click", () => {
        let btnid = btnPlus.id.split("pl")[1];
        cart[btnid] = cart[btnid] + 1;
        document.getElementById(`qyt${btnid}`).innerText = cart[btnid];
        checkOut(cart);
        localStorage.setItem("cart", JSON.stringify(cart));
      });
    });

    btndels.forEach((btndel) => {
      btndel.addEventListener("click", () => {
        let btnid = btndel.id.split("del")[1];
        delete cart[btnid];
        localStorage.setItem("cart", JSON.stringify(cart));
        window.location.replace("http://localhost:8000/shop/cart");
      });
    });
  });
}

async function get(key) {
  let result = await fetch("", {
    headers: {
      "X-CSRFToken": csrf,
    },
    method: "POST",
    mode: "same-origin",
    body: JSON.stringify(key),
  });
  return (await result.json())[0].fields;
}
