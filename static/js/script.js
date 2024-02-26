



//localStorage.removeItem("selectedItem");
//localStorage.removeItem("orderArray");

/*
const order_div = document.getElementById("display_order");
let orderArray = JSON.parse(localStorage.getItem("orderArray")) || [];
orderArray = orderArray.map(item => ({
    ...item,
    default_price: parseFloat(item.default_price).toFixed(2),
    default_price: parseFloat(item.default_price).toFixed(2)

}));
updateOrderDisplay();

//console.log(orderArray);

*/

let order_div = document.getElementById("display_order");
let total_cost = document.getElementById("total_cost");

let orderArray = JSON.parse(localStorage.getItem("orderArray")) || [];

if (orderArray.length > 0) {
    orderArray.map((entry, index) => `
    ${entry.product_id}
    <br>
    ${entry.product_name}
    <br>
    ${entry.price}
    <br>
    ${entry.totalPrice}
    <br>         
        `).join('');
} //LETS SEE IF THIS WORKS. DID IT AFTER A DRINK


const jsonData = JSON.stringify(orderArray);
document.getElementById('orderData').value = jsonData;

//FIND A WAY TO MAKE EVERY FUNCTION HERE ONLY EXECUTE ON A CERTAIN PAGE



console.log(jsonData)

//function updateOrderDisplay() {
if (orderArray.length > 0) {
    order_div.innerHTML = orderArray.map((entry, index) => `
            ${entry.product_name} (x ${entry.product_quantity})<br>
            &pound;${entry.price}<br>
            <br>
            <span id="delete_item" data-index="${index}"><i class="btn fa-solid fa-trash fa-xl"></i></span>
            <br><br>
        `).join('');

    let totalSum = orderArray.reduce((accumulator, entry) => {
        // Convert price to float before adding
        entry.price = parseFloat(entry.price);

        // Make sure the conversion was successful
        if (isNaN(entry.price)) {
            console.error("Failed to convert price to float:", entry);
        }

        return accumulator + entry.price;
    }, 0);

    // Round to two decimal places
    totalSum = totalSum.toFixed(2);

    total_cost.innerHTML = (`Total: ${totalSum}`); // Display the rounded total
    //console.log(`The total sum is ${totalSum} and its type is ${typeof totalSum}`);





    // Add event listeners for delete buttons
    const deleteButtons = order_div.querySelectorAll('#delete_item');
    deleteButtons.forEach(button => {
        button.addEventListener('click', () => deleteItem(button.dataset.index));
    });
} else {
    order_div.innerHTML = "Your basket is empty";
}
//}

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
    document.getElementById('quantity-div').innerHTML = 1;
    const confirmBtn = document.querySelector('.select-product-btn');

    modal.classList.add("show");

    //const increaseBtn = document.getElementById('increase-quantity');
    const decreaseBtn = document.getElementById('decrease-quantity');
    //increaseBtn.addEventListener('click', () => updateQuantity(true));
    decreaseBtn.addEventListener('click', () => updateQuantity(false));

    confirmBtn.addEventListener('click', () => confirmAndClose());

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
            default_price = parseFloat(foundProduct.default_price).toFixed(2);
            //product_quantity = 1;
            msg = "Product was found";
            //console.log(`A product was found and its default price is ${default_price}`);
        } else {

            product_id = productIdFromBtn;
            product_name = productNameFromBtn;
            default_price = parseFloat(productPriceFromBtn).toFixed(2);;
            //product_quantity = 1;
            msg = "Product was NOT found";
            //console.log(`A product was found and its default price is ${default_price}`);

            insertNewProduct = {
                product_id: product_id,
                product_name: product_name,
                default_price: parseFloat(default_price).toFixed(2),
                //product_quantity: 1,
                price: 0.00
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
    //if (product_quantity) { product_quantity = parseFloat(product_quantity); }
    console.log(product_id);

    const pullOrderArrayIndex = orderArray.findIndex(a => a.product_id == product_id);

    if (pullOrderArrayIndex !== -1) {

        orderArray[pullOrderArrayIndex].product_quantity += 1;
        document.getElementById('quantity-div').innerHTML = orderArray[pullOrderArrayIndex].product_quantity;

        //document.getElementById('display_product_name').innerHTML = orderArray[pullOrderArrayIndex].product_name;

        orderArray[pullOrderArrayIndex].price_calc = parseFloat(orderArray[pullOrderArrayIndex].default_price).toFixed(2) * orderArray[pullOrderArrayIndex].product_quantity;
        orderArray[pullOrderArrayIndex].price = parseFloat(orderArray[pullOrderArrayIndex].price_calc).toFixed(2);
       


        //document.getElementById('display_product_price').innerHTML = orderArray[pullOrderArrayIndex].price;



        // Save the updated order array to local storage
        localStorage.setItem("orderArray", JSON.stringify(orderArray));



        //console.log("Product quantity updated successfully!");
        //console.log(orderArray);
        console.log(`The quantity is now ${orderArray[pullOrderArrayIndex].product_quantity}`)
    } else {
        console.log("Product not found in the order array");
    }
    //updateOrderDisplay();
}







// Confirm order and close modal function
function confirmAndClose() {
    // Find the index of the item to update in orderArray
    //const existingIndex = orderArray.findIndex(i => i.product_id === selectedItem.product_id);

    //if (existingIndex !== -1) {
    //    orderArray[existingIndex] = { ...selectedItem }; // Create a new copy
    //} else {
    //     orderArray.push(selectedItem);
    // }

    // localStorage.setItem("orderArray", JSON.stringify(orderArray));
    //selectedItem = [];
    //updateOrderDisplay();


    document.getElementById("modal-div").classList.remove("show");
    document.getElementById("modal-div").classList.add("hide");
}

