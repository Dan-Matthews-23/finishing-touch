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



//const removeItemBtn = document.getElementById("remove-item-btn");
//addEventListener("click", function (event) {
//    if (event.target === removeItemBtn) {
//        removeItem();
//    }
//});






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
const product_id_div = document.getElementById("order-product-ID");
const product_name_div = document.getElementById("display-order-product-name");
const product_quantity_div = document.getElementById("display-order-product-quantity");
const product_price_div = document.getElementById("display-order-product-price");
const quantity_counter = document.getElementById("quantity");

// These fields come from the for() loop. They are values of the database fields that are itterated in i.sandwich_items
const product_id = document.getElementById("product_id").value;
const product_name = document.getElementById("product_name").value;
const product_price = document.getElementById("product_price").value;

// Set the value of product_price to a float
const price = parseFloat(product_price).toFixed(2);


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
        modal.style.display = "none";
        populateOrder();

    }
});
// ---



// Set default quantity to 1 and price to (1x quantity)
let quantity = 1;
let new_price = product_price;
quantity_counter.innerHTML = quantity;
product_price_div.innerHTML = `£${new_price}`;
// ---

const existingOrder = JSON.parse(localStorage.getItem("existingOrder")) || [];

// Functions
function increaseQuantity() {
    quantity += 1;
    new_price = (quantity * price).toFixed(2);
    quantity_counter.innerHTML = quantity;
    product_price_div.innerHTML = `£${new_price}`;
}

function decreaseQuantity() {
    quantity = Math.max(quantity - 1, 1);
    currentPrice = (quantity * price).toFixed(2);
    quantity_counter.innerHTML = quantity;
    product_price_div.innerHTML = `£${new_price}`;
}

function populateOrder() {
    const orderList = {
        orderProductID: product_id,
        orderProductName: product_name,
        orderQuantity: quantity,
        orderPrice: new_price,
    };
    existingOrder.push(orderList);
    localStorage.setItem("existingOrder", JSON.stringify(existingOrder));
    console.log(existingOrder)

    product_name_div.innerHTML = `${product_name}`;
    product_quantity_div.innerHTML = `X ${quantity}`;
    product_price_div.innerHTML = `£${new_price}`;

    console.log(`The product id is ${product_id} and its type is ${typeof product_id}`);
    console.log(`The product name is ${product_name} and its type is ${typeof product_name}`);
    //console.log(document.getElementById("product_name"))
    console.log(`The product quantity is ${quantity} and its type is ${typeof quantity}`);
    console.log(`The product price is ${new_price} and its type is ${typeof new_price}`);

}



//existingOrder.length = 0; // Reset the array


