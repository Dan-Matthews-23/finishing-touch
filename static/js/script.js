



//localStorage.removeItem("selectedItem");
//localStorage.removeItem("orderArray");


const order_div = document.getElementById("display_order");
let orderArray = JSON.parse(localStorage.getItem("orderArray")) || [];
orderArray = orderArray.map(item => ({
    ...item,
    default_price: parseFloat(item.default_price).toFixed(2),
    default_price: parseFloat(item.default_price).toFixed(2)

}));
updateOrderDisplay();

//console.log(orderArray);



function updateOrderDisplay() {
    if (orderArray.length > 0) {
        order_div.innerHTML = orderArray.map((entry, index) => `
            ${entry.product_name} (x ${entry.product_quantity})<br>
            &pound;${entry.default_price}<br>
            <br>
            <span id="delete_item" data-index="${index}"><i class="btn fa-solid fa-trash fa-xl"></i></span>
            <br><br>
        `).join('');

        // Add event listeners for delete buttons
        const deleteButtons = order_div.querySelectorAll('#delete_item');
        deleteButtons.forEach(button => {
            button.addEventListener('click', () => deleteItem(button.dataset.index));
        });

    } else {
        order_div.innerHTML = "Your basket is empty";
    }
}

// Function to delete an item
function deleteItem(index) {
    orderArray.splice(index, 1);
    localStorage.setItem("orderArray", JSON.stringify(orderArray));
    updateOrderDisplay();
}

// Open modal buttons
const selectProductBtns = document.querySelectorAll('.open-modal');
selectProductBtns.forEach(btn => {
    btn.addEventListener('click', openModal);
});

// Modal Logic
function openModal(event) {

    const modal = document.getElementById("modal-div");
    const quantityDiv = document.getElementById('quantity-div');
    const confirmBtn = document.querySelector('.select-product-btn');

    modal.classList.add("show");

    //const increaseBtn = document.getElementById('increase-quantity');
    const decreaseBtn = document.getElementById('decrease-quantity');
    //increaseBtn.addEventListener('click', () => updateQuantity(true));
    decreaseBtn.addEventListener('click', () => updateQuantity(false));

    confirmBtn.addEventListener('click', () => confirmAndClose(selectedItem));

    // Close modal
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.classList.remove("show");
            modal.classList.add("hide");
        }
    }
    document.querySelector('.close').onclick = function () {
        modal.classList.remove("show");
        modal.classList.add("hide");
    }
}

const openModalButtons = document.querySelectorAll('.open-modal');
openModalButtons.forEach(modalBtn => {
    modalBtn.addEventListener('click', function (event) {

        const productIdFromBtn = modalBtn.value;
        const productNameFromBtn = this.dataset.productName;
        const productPriceFromBtn = parseFloat(this.dataset.productPrice);
        // //console.log(`Value for defaul price from btn is ${productPriceFromBtn}`);

        ////console.log(`This product has an ID of ${productIdFromBtn}, its name is ${productNameFromBtn} and its price is ${productPriceFromBtn}`);
        ////console.log(`The typeof ID is ${typeof productIdFromBtn}. The typeof product_name is  is ${typeof productNameFromBtn}. The typeof price is ${typeof productPriceFromBtn} `)

        // Using find()
        const foundProduct = orderArray.find(item => item.product_id === productIdFromBtn);
        if (foundProduct) {
            ////console.log(foundProduct);
            // //console.log(foundProduct.product_name);
            product_id = productIdFromBtn;
            product_name = foundProduct.product_name;
            default_price = foundProduct.default_price;
            //product_quantity = 1;
            msg = "Product was found";
            //console.log(`A product was found and its default price is ${default_price}`);
        } else {

            product_id = productIdFromBtn;
            product_name = productNameFromBtn;
            default_price = productPriceFromBtn;
            //product_quantity = 1;
            msg = "Product was NOT found";
            //console.log(`A product was found and its default price is ${default_price}`);

            insertNewProduct = {
                product_id: product_id,
                product_name: product_name,
                default_price: default_price,
                product_quantity: 1,
                price: 0
            };
            orderArray.push(insertNewProduct);
            ////console.log(`Product not found, so we have added a new item with ID of ${productId}, name of ${product_name} and price of ${default_price}`);
            ////console.log(orderArray);
            localStorage.setItem("orderArray", JSON.stringify(orderArray));
        }
        const increaseBtn = document.getElementById('increase-quantity');
        //const decreaseBtn = document.getElementById('decrease-quantity');
        increaseBtn.addEventListener('click', () => updateQuantity(product_id, product_name, default_price));
        //decreaseBtn.addEventListener('click', () => updateQuantity(false));

        //const increaseQuantityBtn = document.querySelectorAll('.select-product-btn');
        //increaseQuantityBtn.forEach(button => {
        //button.addEventListener('click', function (event) {
        //updateQuantity(product_id, product_name, default_price);

        //});
        //});
    });
});


function updateQuantity(product_id, product_name, default_price) { // Pass product_id if not using event

    if (product_id) { product_id = parseInt(product_id); }
    if (default_price) { default_price = parseFloat(default_price); }
    //if (product_quantity) { product_quantity = parseInt(product_quantity); }
    console.log(product_id);

    const pullOrderArrayIndex = orderArray.findIndex(a => a.product_id == product_id);

    if (pullOrderArrayIndex !== -1) {
        // Update the product quantity and price
        orderArray[pullOrderArrayIndex].product_quantity += 1;
        orderArray[pullOrderArrayIndex].price = orderArray[pullOrderArrayIndex].default_price * orderArray[pullOrderArrayIndex].product_quantity;

        // Save the updated order array to local storage
        localStorage.setItem("orderArray", JSON.stringify(orderArray));

        //console.log("Product quantity updated successfully!");
        //console.log(orderArray);
        console.log(`The quantity is now ${orderArray[pullOrderArrayIndex].product_quantity}`)
    } else {
        console.log("Product not found in the order array");
    }











    /*if (pullOrderArray) {
        console.log(`In updateQuantity function, a product was found`);
        //console.log(pullOrderArray);
        pullOrderArray.product_quantity += 1;
        let new_price = parseFloat(pullOrderArray.default_price * pullOrderArray.product_quantity);
        //console.log(`The quantity is ${pullOrderArray.product_quantity}`);
        //product_quantity = pullOrderArray.product_quantity;
        console.log(`The new quantity is ${pullOrderArray.product_quantity} with type of ${typeof pullOrderArray.product_quantity}. The default price is ${pullOrderArray.default_price} with type of ${pullOrderArray.default_price}. The new price is ${new_price} with type of ${typeof new_price}`);
        pullOrderArray.price = new_price;
       // orderArray.update(pullOrderArray);
        localStorage.setItem("orderArray", JSON.stringify(orderArray));
        //pullOrderArray = [];
        console.log(orderArray);*/





    //} 






    ////console.log(`In updateQuantity function, this product has an ID of ${product_id}, its name is ${product_name} and its price is ${default_price}`);// and the quantity is ${product_quantity}`);
    ////console.log(`In updateQuantity function, the typeof ID is ${typeof product_id}. The typeof product_name is  is ${typeof product_name}. The typeof price is ${typeof default_price}.`);// The typeof quantity is ${typeof product_quantity} `);
    ////console.log(msg);
    ////console.log(product_quantity);


    /* if (isIncrease) {
        const itemIndex = orderArray.findIndex(item => item.product_id === productId);

        ////console.log(`ID is ${productId} and its type is ${typeof productId}`)
        if (itemIndex !== -1) {
            //console.log(`Yes, there is an item here with the product ID of ${productId}. We will update the quantity to ${orderArray[itemIndex].product_quantity}`);
            //let new_quantity = 0;
            //orderArray[itemIndex].product_quantity += 1;

            //orderArray[itemIndex].product_quantity = new_quantity; // Update existing property
            //orderArray[itemIndex].product_quantity = productName,
            //orderArray[itemIndex].product_name,
            //default_price: parseFloat(productPrice),
            //default_price: parseFloat(productPrice),
            //product_quantity: new_quantity

            //orderArray[itemIndex].update(new_values);
            //localStorage.setItem("orderArray", JSON.stringify(orderArray));
            //new_values = [];
            ////console.log(orderArray);
            ////console.log("The quantity was increased. It is now " + orderArray[itemIndex].product_quantity);
            ////console.log(`The index is ${itemIndex}`)
            ////console.log(`The product ID is ${orderArray[itemIndex].product_id} and its type is ${typeof orderArray[itemIndex].product_id} `)
            //return productId;
        } else {
            /*
            let quantity = 0;
            quantity += 1;
            newItem = {
                product_id: productId,
                product_name: productName,
                default_price: parseFloat(productPrice),
                default_price: parseFloat(productPrice),
                product_quantity: quantity
            };
            orderArray.push(newItem);
            //console.log(`Item not found, so we've created it instead. The product ID is ${productId} and its type is ${typeof productId}`);
            ////console.log(itemIndex);
            ////console.log(orderArray);
            ////console.log(`All details have been pulled from the orderArray and are: Product ID: ${productId}, Product Name: ${productName}  `)
        }
    } else {
        const itemIndex = orderArray.findIndex(item => item.product_id === productId);
        if (itemIndex !== -1) { // Check for item before decreasing
            //console.log(itemIndex)
            orderArray[itemIndex].product_quantity = Math.max(orderArray[itemIndex].product_quantity - 1, 1);
            //console.log("The quantity was decreased");
        }
    }*/
}







// Confirm order and close modal function
function confirmAndClose(selectedItem) {
    // Find the index of the item to update in orderArray
    const existingIndex = orderArray.findIndex(i => i.product_id === selectedItem.product_id);

    if (existingIndex !== -1) {
        orderArray[existingIndex] = { ...selectedItem }; // Create a new copy
    } else {
        orderArray.push(selectedItem);
    }

    localStorage.setItem("orderArray", JSON.stringify(orderArray));
    selectedItem = [];
    updateOrderDisplay();


    document.getElementById("modal-div").classList.remove("show");
    document.getElementById("modal-div").classList.add("hide");
}

