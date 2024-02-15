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

let quantity = 0;

const quantityCount = document.getElementById("quantity");
quantityCount.innerHTML = quantity;

const increaseIcon = document.querySelector("increase-quantity-icon");
const decreaseIcon = document.querySelector("decrease-quantity-icon");

const increaseQuantityBtn = document.getElementById("increase-quantity");
const decreaseQuantityBtn = document.getElementById("decrease-quantity");

addEventListener("click", function (event) {
    if (event.target === increaseQuantityBtn || event.target === increaseIcon) {         
        increaseQuantity();        
    } else if (event.target === decreaseQuantityBtn || event.target === decreaseIcon) {
        decreaseQuantity();        
    }
});

function increaseQuantity() {
    quantity += 1;   
    quantityCount.innerHTML = quantity;
}

function decreaseQuantity() {
    quantity = Math.max(quantity - 1, 0);    
    quantityCount.innerHTML = quantity;
}


