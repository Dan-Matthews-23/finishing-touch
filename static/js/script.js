




/*
//const removeItemBtn = document.getElementById("remove-item-btn");
//addEventListener("click", function (event) {
//    if (event.target === removeItemBtn) {
//        removeItem();
//    }
//});




// Assigning the hidden <p> to a variable
const itemAddedP = document.getElementById("item-added");


// THE SECOND PRODUCT MAY NOT BE ADDING TO THE ORDER BECAUSE I AM CALLING THE ID. IDS CAN ONLY BE CALLED ONCE. lOOK TO SEE IF YOU CAN DO THIS


// Assigning variables to buttons
const addToBasket = document.getElementById("add-to-basket");
const increaseQuantityBtn = document.getElementById("increase-quantity");
const decreaseQuantityBtn = document.getElementById("decrease-quantity");





*/


const modal = document.getElementById("modal-div");

const selectProductBtns = document.querySelectorAll('.select-product-btn');
selectProductBtns.forEach(clickedButton => {
    clickedButton.addEventListener('click', function (event) {        
        modal.classList.add("show");
        
        const productId = this.dataset.productId; // Use 'this' to refer to the clicked button        
        const productName = this.dataset.productName;
        const productPrice = this.dataset.productPrice;
        const productQuantity = this.dataset.productQuantity;

        selectedItem = {
            product_id: productId,
            product_name: productName,
            product_price: productPrice,
            product_quantity: productQuantity
        };

        // Get Order Details div
        const order_div = document.getElementById("display_order");
        order_div.innerHTML =
            "Product ID: " + selectedItem.product_id + "<br>" +
            "Product Name: " + selectedItem.product_name + "<br>" +
            "Product Price: $" + selectedItem.product_price + "<br>" +
            "Product Quantity: " + selectedItem.product_quantity;


        console.log(productId);
        console.log(productName);
        console.log(productPrice);
        console.log(productQuantity);


    });
});



// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.classList.remove("show");
    }
}

const span = document.getElementsByClassName("close")[0];
span.onclick = function () {
    modal.classList.remove("show");
}

// TOMORROW YOU NEED TO:

// sHOW/HIDE THE ADD TO BASKET BUTTON ONCE CLICKED
// ADD THE ORDER TO A SEPERATE ARRAY SO THAT THE VALUES ARE NOT OVERRIDDEN
// DISPLAY THAAT ARRAY RATHER THAN THE CURRENT SO THAT THE FULL ORDER IS DISPLAYED, NOT JUST THE ONE THAT'S CLICKED
// FIX THE QUALITY THING. 



/*


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
        btn.style.display = "none";
        itemAddedP.style.display = "block";
        populateOrder();

    }
});
// ---



// Set default quantity to 1 and price to (1x quantity)
let quantity = 1;
let new_price = product_price;
quantity_counter.innerHTML = quantity;
//product_price_div.innerHTML = `£${new_price}`;
// ---

const existingOrder = JSON.parse(localStorage.getItem("existingOrder")) || [];
const check_array = existingOrder.some(orderProduct => orderProduct.orderProductID === product_id);
if (check_array) {
    // Product ID already exists in the array
    btn.style.display = "none";
    itemAddedP.style.display = "block";
    // Handle the existing product (e.g., update quantity, remove, display a message)
} else {
    btn.style.display = "block";
    itemAddedP.style.display = "none";
}











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
    const existingOrder = JSON.parse(localStorage.getItem("existingOrder")) || [];

    const orderProductIDExists = existingOrder.some(orderProduct => orderProduct.orderProductID === product_id);

    if (orderProductIDExists) {
        // Product ID already exists in the array
        console.log("Product with ID", product_id, "already exists in the order.");
        // Handle the existing product (e.g., update quantity, remove, display a message)
    } else {



        const orderList = {
            orderProductID: product_id,
            orderProductName: product_name,
            orderQuantity: quantity,
            orderPrice: new_price,
        };

        existingOrder.push(orderList);
        localStorage.setItem("existingOrder", JSON.stringify(existingOrder));
        console.log(existingOrder)

        //product_name_div.innerHTML = `${product_name}`;
        //product_quantity_div.innerHTML = `X ${quantity}`;
        //product_price_div.innerHTML = `£${new_price}`;

        const retrive_order_array = JSON.parse(localStorage.getItem("existingOrder")) || [];

        display_order.innerHTML = retrive_order_array.map(entry => `
          
          <li class="order-list-styling">${entry.orderProductName}</li>
          <li class="order-list-styling">(X)${entry.orderQuantity}</li>
          <li class="order-list-styling">£${entry.orderPrice}</li>`).join('');
    }
}

const retrive_order_array = JSON.parse(localStorage.getItem("existingOrder")) || [];
display_order.innerHTML = retrive_order_array.map(entry => `
    
    <li class="order-list-styling">${entry.orderProductName}</li>
    <li class="order-list-styling">(X)${entry.orderQuantity}</li>
    <li class="order-list-styling">£${entry.orderPrice}</li>`).join('');






//console.log(`The product id is ${product_id} and its type is ${typeof product_id}`);
//console.log(`The product name is ${product_name} and its type is ${typeof product_name}`);
//console.log(document.getElementById("product_name"))
//console.log(`The product quantity is ${quantity} and its type is ${typeof quantity}`);
//console.log(`The product price is ${new_price} and its type is ${typeof new_price}`);






//localStorage.removeItem("existingOrder");
// Reset the array




const selectProductButton = document.querySelectorAll('.select-product-btn');
selectProductButton.forEach(button => {
    button.addEventListener("click", function (event) {

        const productIds = document.querySelectorAll('.product-id');
        const productIdValues = Array.from(productIds).map(input => input.value);
        console.log(productIdValues);

        const productNames = document.querySelectorAll('.product-name');
        const productNameValues = Array.from(productNames).map(input => input.value);
        console.log(productNameValues);

        const productPrices = document.querySelectorAll('.product-prices');
        const productPricesValues = Array.from(productPrices).map(input => input.value);
        console.log(productPricesValues);

        const combinedProducts = [];
        for (let i = 0; i < productIdValues.length; i++) {
            combinedProducts.push({
                id: productIdValues[i],
                name: productNameValues[i],
                price: productPricesValues[i]
            });
        }
        console.log(combinedProducts)
        // Code to execute when a button is clicked
        console.log("Worked");
    });
});*/