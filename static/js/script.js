//localStorage.removeItem("selectedItems");
//localStorage.removeItem("orderArray");

// Reset the array


// Get Order Details div
const order_div = document.getElementById("display_order");
const orderArray = JSON.parse(localStorage.getItem("orderArray")) || [];
if (orderArray.length > 0) {
    //console.log(orderArray.length)
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

        const increaseQuantityBtn = document.getElementById("increase-quantity");
        const decreaseQuantityBtn = document.getElementById("decrease-quantity");

        increaseQuantityBtn.addEventListener('click', increaseQuantity);
        decreaseQuantityBtn.addEventListener('click', decreaseQuantity);


        //let new_price = 0;
        let quantity = 1;

        const modal = document.getElementById("modal-div");
        const quantity_div = document.getElementById('quantity-div');
        quantity_div.innerHTML = quantity;

        modal.classList.add("show");
        const product_price_div = document.getElementById("display-order-product-price");
        //const productId = this.dataset.productId;
        //const productName = this.dataset.productName;
        //const productPrice = this.dataset.productPrice;

        selectedItem = {
            product_id: this.dataset.productId,
            product_name: this.dataset.productName,
            product_price: this.dataset.productPrice,
            product_quantity: 1
        };
        
        function increaseQuantity() {
            quantity += 1;
            selectedItem.quantity = quantity
            total = (selectedItem.quantity * selectedItem.product_price).toFixed(2);
            quantity_div.innerHTML = selectedItem.quantity;
        }

        function decreaseQuantity() {
            quantity = Math.max(quantity - 1, 1);
            selectedItem.quantity = quantity
            total = (selectedItem.quantity * selectedItem.product_price).toFixed(2);
            quantity_div.innerHTML = selectedItem.quantity;         

        }



        const confirmOrder = document.querySelectorAll('.select-product-btn');

        confirmOrder.forEach(clickedConfirmOrderBtn => {
            clickedConfirmOrderBtn.addEventListener('click', function (event) {

                const existingIndex = orderArray.findIndex(item => item.product_id === selectedItem.productId);

                if (existingIndex !== -1) {
                    // Update existing item
                    console.log("The current quantity is " + selectedItem.product_quantity)
                    orderArray[existingIndex] = selectedItem;
                    localStorage.setItem("orderArray", JSON.stringify(orderArray));
                    //console.log("Product updated:", selectedItem);
                } else {
                    // Add new item if ID doesn't exist
                    orderArray.push(selectedItem);
                    localStorage.setItem("orderArray", JSON.stringify(orderArray));
                    //console.log("Product added:", selectedItem);
                }

                modal.classList.remove("show");
                modal.classList.add("hide");
                //clickedOpenModalBtn.classList.add("hide");

                const pullOrderArray = JSON.parse(localStorage.getItem("orderArray")) || [];

                order_div.innerHTML = pullOrderArray.map(entry => `
                ${entry.product_name} (x ${entry.product_quantity})<br>
                &pound;${entry.product_price}<br>
                <br><br><br>
`               ).join('');
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



