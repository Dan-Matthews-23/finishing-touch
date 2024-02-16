// Get the modal
var modal = document.getElementById("select-product-modal");

// Get the button that opens the modal
var btn = document.getElementById("select-product-btn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function () {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

let quantity = 1;
let currentPrice = 0;



const displayOrderProductName = document.getElementById("display-order-product-name");
const displayOrderProductQuantity = document.getElementById("display-order-product-quantity");
const displayOrderProductPrice = document.getElementById("display-order-product-price");


const createOrderBtn = document.getElementById("add-to-basket");
const existingOrder = JSON.parse(localStorage.getItem("existingOrder")) || [];

const productID = document.getElementById("product-id").value;
const productName = document.getElementById("product-name").value;

const databasePrice = document.getElementById("product-price-hidden").value;
const displayPrice = document.getElementById("product-price");

const price = parseFloat(databasePrice).toFixed(2);

const quantityCount = document.getElementById("quantity");

quantityCount.innerHTML = quantity;
displayPrice.innerHTML = `£${price}`;


const increaseQuantityBtn = document.getElementById("increase-quantity");
const decreaseQuantityBtn = document.getElementById("decrease-quantity");

addEventListener("click", function (event) {
    if (event.target === increaseQuantityBtn) {
        increaseQuantity();
    } else if (event.target === decreaseQuantityBtn) {
        decreaseQuantity();
    }
});

addEventListener("click", function (event) {
    if (event.target === createOrderBtn) {
        populateOrder();
        modal.style.display = "none";
    }
});

function increaseQuantity() {
    quantity += 1;
    currentPrice = (quantity * price).toFixed(2);
    quantityCount.innerHTML = quantity;
    displayPrice.innerHTML = `£${currentPrice}`;
}

function decreaseQuantity() {
    quantity = Math.max(quantity - 1, 1);
    currentPrice = (quantity * price).toFixed(2);
    quantityCount.innerHTML = quantity;
    displayPrice.innerHTML = `£${currentPrice}`;
}



function populateOrder() {
    const orderList = {
        orderProductID: productID,
        orderProductName: productName,
        orderQuantity: quantity,
        orderPrice: currentPrice,
    };
    existingOrder.push(orderList);
    localStorage.setItem("existingOrder", JSON.stringify(existingOrder));
    console.log(existingOrder)





    displayOrderProductName.innerHTML = `${productName}`;
    displayOrderProductQuantity.innerHTML = quantity;
    displayOrderProductPrice.innerHTML = `£${currentPrice}`;

}






