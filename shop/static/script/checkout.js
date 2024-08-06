let cart = {};
if (localStorage.getItem("cart")) {
  cart = JSON.parse(localStorage.getItem("cart"));

  if (Object.keys(cart).length == 0) {
    document.getElementById("liPrd").innerHTML = `
     <li
          class="list-group-item d-flex justify-content-between align-items-center"
          style="background-color: #1b1f22"
        >
          <div class="ms-2 me-auto text-light">
            <div class="fw-bold text-light">No Item in cart</div>
            Sub Total: 0
          </div>
          <span
            class="badge rounded-pill text-light"
            style="background-color: #616161"
            >0</span
          >
        </li>
     `;
  } else {
    fetchItem(cart);
    fetchAmout(cart);
    enableButton()
  }
} else {
  document.getElementById("liPrd").innerHTML = `
     <li
          class="list-group-item d-flex justify-content-between align-items-center"
          style="background-color: #1b1f22"
        >
          <div class="ms-2 me-auto text-light">
            <div class="fw-bold text-light">No Item in cart</div>
            Sub Total: 0
          </div>
          <span
            class="badge rounded-pill text-light"
            style="background-color: #616161"
            >0</span
          >
        </li>
     `;
}

async function fetchItem(cart) {
  let p = "";
  let keys = Object.keys(cart);
  keys.forEach(async (key) => {
    if(cart[key] != 0 ){
      let data = await get(key);
      let qyt = 0 + cart[key];
      let pr = 0 + data.price;
      let subTotal = qyt * pr;
      let p1 = `<li
          class="list-group-item d-flex justify-content-between align-items-center"
          style="background-color: #1b1f22"
        >
          <div class="ms-2 me-auto text-light">
            <div class="fw-bold text-light">${await data.product_name}</div>
            Sub Total: ${subTotal}
          </div>
          <span
            class="badge rounded-pill text-light"
            style="background-color: #616161"
            >${cart[key]}</span
          >
        </li>`;

      p = p + p1;
      document.getElementById("liPrd").innerHTML = p;
    }
  });
}

async function fetchAmout(cart) {
   let p = 0;
   let keys = Object.keys(cart);
   keys.forEach(async (key) => {
    let data = await get(key);
    let qyt = 0 + cart[key];
    let pr = 0 + data.price;
    p = p + qyt * pr;
    document.getElementById(
      "tlamn"
    ).innerHTML = `<b>Total Amount:</b> $ ${p}.00`;
   })
}

async function get(key) {
  let result = await fetch("http://localhost:8000/shop/cart/", {
    headers: {
      "X-CSRFToken": "ue4im0sXxwK9sGX4jdHtIcaJWSsls8Kp",
    },
    method: "POST",
    mode: "same-origin",
    body: JSON.stringify(key),
  });
  return (await result.json())[0].fields;
}

function enableButton () {
 document.getElementById("plor").disabled = false;
}
