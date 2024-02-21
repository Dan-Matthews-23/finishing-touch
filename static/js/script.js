



//localStorage.removeItem("selectedItem");
//localStorage.removeItem("orderArray");


const order_div = document.getElementById("display_order");
let orderArray = JSON.parse(localStorage.getItem("orderArray")) || [];
orderArray = orderArray.map(item => ({
    ...item,
    product_price: parseFloat(item.product_price).toFixed(2),
    original_price: parseFloat(item.original_price).toFixed(2)

}));
updateOrderDisplay();

//console.log(orderArray);



function updateOrderDisplay() {
    if (orderArray.length > 0) {
        order_div.innerHTML = orderArray.map((entry, index) => `
            ${entry.product_name} (x ${entry.product_quantity})<br>
            &pound;${entry.product_price}<br>
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














    //let selectedItem;
    //if (existingItem) {
    //selectedItem = { ...existingItem }; // Create a copy
    //} else {
    //selectedItem = {
    //product_id: event.target.dataset.productId,
    //product_name: event.target.dataset.productName,
    //product_price: parseFloat(event.target.dataset.productPrice),
    //original_price: parseFloat(event.target.dataset.productPrice),
    //product_quantity: 1
    //};
    //}
    //console.log("selectedItem in openModal:", selectedItem);

    //quantityDiv.innerHTML = selectedItem.product_quantity;

    modal.classList.add("show");

    const increaseBtn = document.getElementById('increase-quantity');
    const decreaseBtn = document.getElementById('decrease-quantity');
    increaseBtn.addEventListener('click', () => updateQuantity(true));
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
openModalButtons.forEach(button => {
    button.addEventListener('click', function (event) {
        const productId = event.target.dataset.productId;
        const productName = event.target.dataset.productName;
        const productPrice = event.target.dataset.productPrice;
        // You now have the data to use or pass to your updateQuantity function
        updateQuantity(true, productId, productName, productPrice); // Example if updateQuantity handles adding 
    });
});


function updateQuantity(isIncrease, productId, productName, productPrice) { // Pass product_id if not using event
    if (isIncrease) {
        const itemIndex = orderArray.findIndex(item => item.product_id === productId);
        if (itemIndex !== -1) {
            orderArray[itemIndex].product_quantity += 1; // Corrected increment
            console.log("The quantity was increased");
        } else {
            newItem = {
                product_id: productId,
                product_name: productName,
                product_price: parseFloat(productPrice),
                original_price: parseFloat(productPrice),
                product_quantity: 1
            };
            orderArray.push(newItem);
            console.log("Item not found, so we've created it instead");
            console.log(itemIndex);
            console.log(orderArray);
            console.log(`All details have been pulled from the orderArray and are: Product ID: ${productId}, Product Name: ${productName}  `)
        }
    } else {
        const itemIndex = orderArray.findIndex(item => item.product_id === product_id);
        if (itemIndex !== -1) { // Check for item before decreasing
            console.log(itemIndex)
            orderArray[itemIndex].product_quantity = Math.max(orderArray[itemIndex].product_quantity - 1, 1);
            console.log("The quantity was decreased");
        }
    }
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

