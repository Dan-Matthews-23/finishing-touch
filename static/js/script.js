//localStorage.removeItem("selectedItem");
//localStorage.removeItem("orderArray");




// Variables
let order_div = document.getElementById("display_order");
let total_cost = document.getElementById("total_cost");
let orderArray = JSON.parse(localStorage.getItem("orderArray")) || [];
const jsonData = JSON.stringify(orderArray);
document.getElementById('orderData').value = jsonData;
const selectProductBtns = document.querySelectorAll('.open-modal');

// Event Listeners
selectProductBtns.forEach(btn => {
    btn.addEventListener('click', openModal);
});



function updateOrder() {
    if (orderArray.length > 0) {
        order_div.innerHTML = orderArray.map((entry, index) => `
            ${entry.product_name} (x ${entry.product_quantity})<br>
            &pound;${entry.price}<br>
            <br>
            <span id="delete_item" data-index="${index}"><i class="btn fa-solid fa-trash fa-xl"></i></span>
            <br><br>
        `).join('');

        let totalSum = orderArray.reduce((accumulator, entry) => {
            const itemPrice = parseFloat(entry.price); // Convert price to number

            if (isNaN(itemPrice)) {
                console.error("Failed to convert price to float:", entry);
                return accumulator; // Skip invalid prices
            }

            return accumulator + itemPrice;
        }, 0);

        totalSum = parseFloat(totalSum).toFixed(2);

        total_cost.innerHTML = (`Total: £${totalSum}`);


        const deleteButtons = order_div.querySelectorAll('#delete_item');
        deleteButtons.forEach(button => {
            button.addEventListener('click', () => deleteItem(button.dataset.index));
        });
    } else {
        order_div.innerHTML = "Your basket is empty";
    }

}




function deleteItem(index) {
    orderArray.splice(index, 1);
    localStorage.setItem("orderArray", JSON.stringify(orderArray));
    updateOrder();
}



function openModal(event) {
    const modal = document.getElementById("modal-div");
    //document.getElementById('quantity-div').innerHTML = 1;
    const confirmBtn = document.querySelector('.select-product-btn');
    modal.classList.add("show");
    //const decreaseBtn = document.getElementById('decrease-quantity');
    //decreaseBtn.addEventListener('click', () => updateQuantity(false));
    confirmBtn.addEventListener('click', () => confirmAndClose());

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
        const productPriceFromBtn = this.dataset.productPrice;
        const foundProduct = orderArray.find(item => item.product_id === productIdFromBtn);
        if (foundProduct) {
            product_id = productIdFromBtn;
            product_name = foundProduct.product_name;
            default_price = foundProduct.default_price;
            const resetQuantity = orderArray.findIndex(a => a.product_id == product_id);
            document.getElementById('quantity-div').innerHTML = orderArray[resetQuantity].product_quantity;
            console.log(orderArray[resetQuantity].product_quantity)
            msg = "Product was found";
        } else {
            document.getElementById('quantity-div').innerHTML = 1;
            product_id = productIdFromBtn;
            product_name = productNameFromBtn;
            default_price = productPriceFromBtn
            msg = "Product was NOT found";
            insertNewProduct = {
                product_id: product_id,
                product_name: product_name,
                default_price: default_price,
                price: 0.00,
            };
            orderArray.push(insertNewProduct);
            localStorage.setItem("orderArray", JSON.stringify(orderArray));
        }
        const increaseBtn = document.getElementById('increase-quantity');
        const decreaseBtn = document.getElementById('decrease-quantity');
        increaseBtn.addEventListener('click', () => increaseQuantity(product_id, product_name, default_price));
        decreaseBtn.addEventListener('click', () => decreaseQuantity(product_id, product_name, default_price));
    });
    updateOrder();
});

function increaseQuantity(product_id, default_price) {
    if (product_id) { product_id = product_id; }
    if (default_price) { default_price = default_price; }
    const pullOrderArrayIndex = orderArray.findIndex(a => a.product_id == product_id);
    if (pullOrderArrayIndex !== -1) {
        if (!isNaN(orderArray[pullOrderArrayIndex].product_quantity)) {
            orderArray[pullOrderArrayIndex].product_quantity += 1;
            // Prevent quantity from going below 0            
        } else {
            orderArray[pullOrderArrayIndex].product_quantity = 1;
        }

        document.getElementById('quantity-div').innerHTML = orderArray[pullOrderArrayIndex].product_quantity;
        orderArray[pullOrderArrayIndex].price = orderArray[pullOrderArrayIndex].default_price * orderArray[pullOrderArrayIndex].product_quantity;
        orderArray[pullOrderArrayIndex].price = orderArray[pullOrderArrayIndex].price.toFixed(2);
        localStorage.setItem("orderArray", JSON.stringify(orderArray));
        //console.log(`The value of produdct_id is ${orderArray[pullOrderArrayIndex].product_id} and its type is ${typeof orderArray[pullOrderArrayIndex].product_id}`);
        //console.log(`The value of product_name is ${orderArray[pullOrderArrayIndex].product_name} and its type is ${typeof orderArray[pullOrderArrayIndex].product_name}`);
        //console.log(`The value of price is ${orderArray[pullOrderArrayIndex].price} and its type is ${typeof orderArray[pullOrderArrayIndex].price}`);
        //console.log(`The value of price_calc is ${orderArray[pullOrderArrayIndex].price_calc} and its type is ${typeof orderArray[pullOrderArrayIndex].price_calc}`);
        //console.log(`The value of quantity is ${orderArray[pullOrderArrayIndex].product_quantity} and its type is ${typeof orderArray[pullOrderArrayIndex].product_quantity}`);
        //console.log(`The value of default_price is ${orderArray[pullOrderArrayIndex].default_price} and its type is ${typeof orderArray[pullOrderArrayIndex].default_price}`);
    } else {
        console.log("Product not found in the order array");
    }
    updateOrder()
}

function decreaseQuantity(product_id, default_price) {
    if (product_id) { product_id = product_id; }
    if (default_price) { default_price = default_price; }
    const pullOrderArrayIndex = orderArray.findIndex(a => a.product_id == product_id);
    if (pullOrderArrayIndex !== -1) {
        if (!isNaN(orderArray[pullOrderArrayIndex].product_quantity)) {
            if (orderArray[pullOrderArrayIndex].product_quantity < 2) {
                orderArray[pullOrderArrayIndex].product_quantity = 1
            } else {
                orderArray[pullOrderArrayIndex].product_quantity -= 1;
            }
            // Prevent quantity from going below 0            
        } else {
            orderArray[pullOrderArrayIndex].product_quantity = 1;
        }

        document.getElementById('quantity-div').innerHTML = orderArray[pullOrderArrayIndex].product_quantity;
        orderArray[pullOrderArrayIndex].price = orderArray[pullOrderArrayIndex].default_price * orderArray[pullOrderArrayIndex].product_quantity;
        orderArray[pullOrderArrayIndex].price = orderArray[pullOrderArrayIndex].price.toFixed(2);
        localStorage.setItem("orderArray", JSON.stringify(orderArray));
        //console.log(`The value of produdct_id is ${orderArray[pullOrderArrayIndex].product_id} and its type is ${typeof orderArray[pullOrderArrayIndex].product_id}`);
        //console.log(`The value of product_name is ${orderArray[pullOrderArrayIndex].product_name} and its type is ${typeof orderArray[pullOrderArrayIndex].product_name}`);
        //console.log(`The value of price is ${orderArray[pullOrderArrayIndex].price} and its type is ${typeof orderArray[pullOrderArrayIndex].price}`);
        //console.log(`The value of price_calc is ${orderArray[pullOrderArrayIndex].price_calc} and its type is ${typeof orderArray[pullOrderArrayIndex].price_calc}`);
        //console.log(`The value of quantity is ${orderArray[pullOrderArrayIndex].product_quantity} and its type is ${typeof orderArray[pullOrderArrayIndex].product_quantity}`);
        //console.log(`The value of default_price is ${orderArray[pullOrderArrayIndex].default_price} and its type is ${typeof orderArray[pullOrderArrayIndex].default_price}`);
    } else {
        console.log("Product not found in the order array");
    }
    updateOrder()
}


function confirmAndClose() {
    document.getElementById("modal-div").classList.remove("show");
    document.getElementById("modal-div").classList.add("hide");
    updateOrder()
}