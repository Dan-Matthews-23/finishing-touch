
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

// This code was adapted from https://www.codingnepalweb.com/star-rating-html-css-javascript-2/ //


// Select all elements with the "i" tag and store them in a NodeList called "stars"
const stars = document.querySelectorAll(".stars i");

// Loop through the "stars" NodeList
stars.forEach((star, index1) => {
    // Add the click event listener (this part stays the same)
    star.addEventListener("click", () => {
        stars.forEach((star, index2) => {
            index1 >= index2 ? star.classList.add("active") : star.classList.remove("active");
            document.getElementById("selected_rating").value = index1 + 1;
        });
    });

    // Add the mouseover event listener for highlighting
    star.addEventListener("mouseover", () => {
        stars.forEach((star, index2) => {
            index1 >= index2 ? star.classList.add("active") : star.classList.remove("active");
        });
    });

    // Add the mouseout event listener to remove highlighting
    star.addEventListener("mouseout", () => {
        stars.forEach((star) => {
            star.classList.remove("active"); // Remove 'active' from all on mouseout
        });
    });
});


