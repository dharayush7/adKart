console.log("working...")

localStorage.removeItem("cart");
cartLink.innerHTML = `0`;

const orderId = document.getElementById("orderId").innerText

document.getElementById("copy").addEventListener("click", () => {
    navigator.clipboard.writeText(orderId);
    document.getElementById("copy").innerText = "copied"
})