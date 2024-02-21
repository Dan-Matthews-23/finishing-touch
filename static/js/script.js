//localStorage.removeItem("selectedItem");
//localStorage.removeItem("orderArray");

// Reset the array



const order_div = document.getElementById("display_order");
let orderArray = JSON.parse(localStorage.getItem("orderArray")) || [];
orderArray = orderArray.map(item => ({
    ...item,
    product_price: parseFloat(item.product_price).toFixed(2),
    original_price: parseFloat(item.original_price).toFixed(2)
}));
updateOrderDisplay();

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
    orderArray.splice(index, 1);  // Remove the item at the given index
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
    const increaseBtn = document.getElementById('increase-quantity');
    const decreaseBtn = document.getElementById('decrease-quantity');
    const confirmBtn = document.querySelector('.select-product-btn');

    let selectedItem = {
        product_id: event.target.dataset.productId,
        product_name: event.target.dataset.productName,
        product_price: parseFloat(event.target.dataset.productPrice),
        original_price: parseFloat(event.target.dataset.productPrice),
        product_quantity: 1
    };

    quantityDiv.innerHTML = selectedItem.product_quantity;
    modal.classList.add("show");

    increaseBtn.addEventListener('click', () => updateQuantity(selectedItem, true));
    decreaseBtn.addEventListener('click', () => updateQuantity(selectedItem, false));
    confirmBtn.addEventListener('click', () => confirmAndClose(selectedItem));

    // Close modal on outside click and close button
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

function updateQuantity(item, isIncrease) {
    if (isIncrease) {
        item.product_quantity++;
    } else {
        item.product_quantity = Math.max(item.product_quantity - 1, 1);
    }

    // Calculate using the original price
    item.product_price = (item.product_quantity * item.original_price).toFixed(2);

    document.getElementById('quantity-div').innerHTML = item.product_quantity;
}



// Confirm order and close modal function
function confirmAndClose(item) {
    const existingIndex = orderArray.findIndex(i => i.product_id === item.product_id);
    if (existingIndex !== -1) {
        orderArray[existingIndex] = item;
    } else {
        orderArray.push(item);
    }
    localStorage.setItem("orderArray", JSON.stringify(orderArray));
    updateOrderDisplay();
    //console.log(item.product_price)

    document.getElementById("modal-div").classList.remove("show");
    document.getElementById("modal-div").classList.add("hide");
}


