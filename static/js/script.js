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

function increaseQuantity() {
    quantity += 1;
    currentPrice = (quantity * price).toFixed(2);
    console.log(`
    The value of the hidden field called databasePrice is ${databasePrice}, and its type is ${typeof databasePrice}.
    The value of quantity is ${quantity} and its type is ${typeof quantity}. 
    The value of price is ${price} and its type is ${typeof price}. 
    The value of final price is ${currentPrice} currently, and the type is ${typeof currentPrice}
    `);
    quantityCount.innerHTML = quantity;
    displayPrice.innerHTML = `£${currentPrice}`;
}

function decreaseQuantity() {
    quantity = Math.max(quantity - 1, 0);
    currentPrice = (quantity * price).toFixed(2);
    console.log(`
    The value of the hidden field called databasePrice is ${databasePrice}, and its type is ${typeof databasePrice}.
    The value of quantity is ${quantity} and its type is ${typeof quantity}. 
    The value of price is ${price} and its type is ${typeof price}. 
    The value of final price is ${currentPrice} currently, and the type is ${typeof currentPrice}
    `);

    quantityCount.innerHTML = quantity;
    displayPrice.innerHTML = `£${currentPrice}`;
}


