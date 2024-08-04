let cartLink = document.getElementById("cartLink");
let pop = document.getElementById("pop")
let body = document.querySelector('.popover-body')

cart = localStorage.getItem('cart')

if(cart){
    jsonCart = JSON.parse(cart);
    cartLink.innerHTML = `(${Object.keys(jsonCart).length})`
}

pop.setAttribute("data-bs-content", `<p>Hi</p>`);

const popoverTriggerList = document.querySelectorAll(
  '[data-bs-toggle="popover"]'
);
const popoverList = [...popoverTriggerList].map(
  (popoverTriggerEl) => new bootstrap.Popover(popoverTriggerEl)
);





