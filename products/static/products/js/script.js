
console.log("WORKED");

let coll = document.getElementsByClassName("collapsible");
let i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    });
}








// Variables
let order_div = document.getElementById("display_order");

let total_cost = document.getElementById("total_cost");
let orderArray = JSON.parse(localStorage.getItem("orderArray")) || [];
basketTotalElement = document.getElementById("basket-total");
const jsonData = JSON.stringify(orderArray);
//document.getElementById('orderData').value = jsonData;


const selectProductBtns = document.querySelectorAll('.open-modal');

// Event Listeners
selectProductBtns.forEach(btn => {
    btn.addEventListener('click', openModal);
});


function openModal(event) {
    const modal = document.getElementById("modal-div");   
    const confirmBtn = document.querySelector('.select-product-btn');
    
    modal.classList.add("show");    
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
        const foundProduct = orderArray.find(item => item.product_id === productIdFromBtn);
        if (foundProduct) {
            product_id = productIdFromBtn;
            document.getElementById('product_test').value = product_id; 

            console.log(product_id)
            const resetQuantity = orderArray.findIndex(a => a.product_id == product_id);   
        } else {
            
            product_id = productIdFromBtn;            
            document.getElementById('product_test').value = product_id; 

            console.log(product_id)
            insertNewProduct = {
                product_id: product_id,                
            };
            orderArray.push(insertNewProduct);
            localStorage.setItem("orderArray", JSON.stringify(orderArray));
        }        
    });   
});





function confirmAndClose(product_id) {
    document.getElementById("modal-div").classList.remove("show");
    document.getElementById("modal-div").classList.add("hide");
    updateOrder()
}
