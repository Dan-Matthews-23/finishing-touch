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



const removeItemBtn = document.getElementById("remove-item-btn");
addEventListener("click", function (event) {
    if (event.target === removeItemBtn) {
        removeItem();
    }
});



// DO ALL OF THESE VARIABLES AGAIN - THEY'RE A MESS!!


// Assigning variables to buttons
const addToBasket = document.getElementById("add-to-basket");
const increaseQuantityBtn = document.getElementById("increase-quantity");
const decreaseQuantityBtn = document.getElementById("decrease-quantity");

// Hidden fields for use in Python
const hidden_product_id = document.getElementById("hidden_product_id");
const hidden_product_name = document.getElementById("hidden_product_name");
const hidden_product_quantity = document.getElementById("hidden_product_quantity");
const hidden_product_price = document.getElementById("hidden_product_price");

// Actual DIV IDs for use in innerHTML section and order details
const showProductID = document.getElementById("order-product-ID");
const showProductName = document.getElementById("display-order-product-name");
const showProductQuantity = document.getElementById("display-order-product-quantity");
const showProductPrice = document.getElementById("display-order-product-price");



// Event Listeners
addEventListener("click", function (event) {
    if (event.target === increaseQuantityBtn) {
        increaseQuantity();
    } else if (event.target === decreaseQuantityBtn) {
        decreaseQuantity();
    }
});

addEventListener("click", function (event) {
    if (event.target === addToBasket) {
        populateOrder();
        modal.style.display = "none";
    }
});
// ---



// Set default quantity to 1 and price to (1x quantity)
let quantity = 1;
let currentPrice = 0;
quantityCount.innerHTML = quantity;
displayPrice.innerHTML = `£${price}`;
// ---

// Pull the values from the for() loop (for i in sandwich_items)
const productID = document.getElementById("product-id").value;
const productName = document.getElementById("product-name").value;
const databasePrice = document.getElementById("product-price-hidden").value;
const displayPrice = document.getElementById("product-price");
// ---













const existingOrder = JSON.parse(localStorage.getItem("existingOrder")) || [];




const price = parseFloat(databasePrice).toFixed(2);

const quantityCount = document.getElementById("quantity");









// Functions
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

    showProductName.innerHTML = `${productName}`;
    showProductQuantity.innerHTML = `X ${quantity}`;
    showProductPrice.innerHTML = `£${currentPrice}`;
    showProductID.innerHTML = `${productID}`;

}



//existingOrder.length = 0; // Reset the array


