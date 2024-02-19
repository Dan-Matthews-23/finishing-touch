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



        let quantity = 1;
        let new_price = 0;

        const modal = document.getElementById("modal-div");
        const quantity_div = document.getElementById('quantity-div');
        quantity_div.innerHTML = quantity;

        modal.classList.add("show");
        const product_price_div = document.getElementById("display-order-product-price");
        const productId = this.dataset.productId;
        const productName = this.dataset.productName;
        const productPrice = this.dataset.productPrice;



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

            //console.log(`Default product price is ${productPrice} and the new price is ${new_price}`);
        }

        function decreaseQuantity() {
            quantity = Math.max(quantity - 1, 1);
            new_price = (quantity * productPrice).toFixed(2);
            quantity_div.innerHTML = quantity;
            product_price_div.innerHTML = `£${new_price}`;
            //console.log(`Default product price is ${productPrice} and the new price is ${new_price}`);

        }

        

        const confirmOrder = document.querySelectorAll('.select-product-btn');

        confirmOrder.forEach(clickedConfirmOrderBtn => {
            clickedConfirmOrderBtn.addEventListener('click', function (event) {

                const existingIndex = orderArray.findIndex(item => item.product_id === productId);

                selectedItem = {
                    product_id: productId,
                    product_name: productName,
                    product_price: new_price,
                    product_quantity: quantity
                };




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



