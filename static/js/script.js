//localStorage.removeItem("selectedItems");
//localStorage.removeItem("orderArray");

// Reset the array

let default_quantity = 1;
const quantity_div = document.querySelectorAll('.quantity-div');
quantity_div.innerHTML = default_quantity;

// Get Order Details div
const order_div = document.getElementById("display_order");
const orderArray = JSON.parse(localStorage.getItem("orderArray")) || [];
if (orderArray.length > 0) {
    console.log(orderArray.length)
    order_div.innerHTML = orderArray.map(entry => `
    ${entry.product_id}<br>
    ${entry.product_name}<br>
    ${entry.product_price}<br>
    ${entry.product_quantity}<br>
    `).join('');
} else {
    order_div.innerHTML = "Your basket is empty";
}

const selectProductBtns = document.querySelectorAll('.open-modal');
selectProductBtns.forEach(clickedOpenModalBtn => {
    clickedOpenModalBtn.addEventListener('click', function (event) {

        const modal = document.getElementById("modal-div");
        quantity = default_quantity

        addEventListener("click", function (event) {
            if (event.target === increaseQuantityBtn) {
                increaseQuantity();
            } else if (event.target === decreaseQuantityBtn) {
                decreaseQuantity();
            }
        });

        function increaseQuantity() {
            quantity += 1;
            new_price = (quantity * productPrice).toFixed(2);
            quantity_div.innerHTML = quantity;
            product_price_div.innerHTML = `£${new_price}`;
        }

        function decreaseQuantity() {
            quantity = Math.max(quantity - 1, 1);
            currentPrice = (quantity * productPrice).toFixed(2);
            quantity_div.innerHTML = quantity;
            product_price_div.innerHTML = `£${new_price}`;
        }

        modal.classList.add("show");
        const product_price_div = document.getElementById("display-order-product-price");
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

        const existingIndex = orderArray.findIndex(item => item.product_id === productId);

        if (existingIndex !== -1) {
            // Update existing item
            orderArray[existingIndex] = selectedItem;
            localStorage.setItem("orderArray", JSON.stringify(orderArray));
            console.log("Product updated:", selectedItem);
        } else {
            // Add new item if ID doesn't exist
            orderArray.push(selectedItem);
            localStorage.setItem("orderArray", JSON.stringify(orderArray));
            console.log("Product added:", selectedItem);
        }

        //orderArray.push(selectedItem);
        //localStorage.setItem("orderArray", JSON.stringify(orderArray));

        const increaseQuantityBtn = document.getElementById("increase-quantity");
        const decreaseQuantityBtn = document.getElementById("decrease-quantity");

        const confirmOrder = document.querySelectorAll('.select-product-btn');

        confirmOrder.forEach(clickedConfirmOrderBtn => {
            clickedConfirmOrderBtn.addEventListener('click', function (event) {

                modal.classList.remove("show");
                modal.classList.add("hide");
                //clickedOpenModalBtn.classList.add("hide");

                const pullOrderArray = JSON.parse(localStorage.getItem("orderArray")) || [];

                /*
                order_div.innerHTML =
                    "Product ID: " + selectedItem.product_id + "<br>" +
                    "Product Name: " + selectedItem.product_name + "<br>" +
                    "Product Price: £" + selectedItem.product_price + "<br>" +
                    "Product Quantity: " + selectedItem.product_quantity;
                
                */
                order_div.innerHTML = pullOrderArray.map(entry => `
                ${entry.product_id}<br>
                ${entry.product_name}<br>
                ${entry.product_price}<br>
                ${entry.product_quantity}<br>
                `).join('');
            });
        });

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function (event) {
            if (event.target == modal) {
                modal.classList.remove("show");
                modal.classList.add("hide");
            }
        }

        const span = document.getElementsByClassName("close")[0];
        span.onclick = function () {
            modal.classList.remove("show");
            modal.classList.add("hide");
        }

    });
});





// TOMORROW YOU NEED TO:

// sHOW/HIDE THE ADD TO BASKET BUTTON ONCE CLICKED
// ADD THE ORDER TO A SEPERATE ARRAY SO THAT THE VALUES ARE NOT OVERRIDDEN
// DISPLAY THAAT ARRAY RATHER THAN THE CURRENT SO THAT THE FULL ORDER IS DISPLAYED, NOT JUST THE ONE THAT'S CLICKED
// FIX THE QUALITY THING. 






// Set the value of product_price to a float
//const price = parseFloat(product_price).toFixed(2);
// Event Listeners


/*
addEventListener("click", function (event) {
    if (event.target === addToBasket) {
        modal.style.display = "none";
        btn.style.display = "none";
        itemAddedP.style.display = "block";
        populateOrder();

    }
});
// ---
*/


// Set default quantity to 1 and price to (1x quantity)

//let new_price = product_price;

//product_price_div.innerHTML = `£${new_price}`;
// ---

/*
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

*/
// Functions



/*
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
});

//const removeItemBtn = document.getElementById("remove-item-btn");
//addEventListener("click", function (event) {
//    if (event.target === removeItemBtn) {
//        removeItem();
//    }
//});







// THE SECOND PRODUCT MAY NOT BE ADDING TO THE ORDER BECAUSE I AM CALLING THE ID. IDS CAN ONLY BE CALLED ONCE. lOOK TO SEE IF YOU CAN DO THIS


// Assigning variables to buttons
const addToBasket = document.getElementById("add-to-basket");
const increaseQuantityBtn = document.getElementById("increase-quantity");
const decreaseQuantityBtn = document.getElementById("decrease-quantity");

*/