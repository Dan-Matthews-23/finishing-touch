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

function clearLocalStorage() {
    //console.log("Order placed successfully!");   
    localStorage.removeItem("selectedItem");
    localStorage.removeItem("orderArray");
}

// Call the function immediately since we're on the confirmation page
clearLocalStorage();