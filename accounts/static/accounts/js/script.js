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

const starRating1 = document.getElementById("star_rating_1");
const starRating2 = document.getElementById("star_rating_2");
const starRating3 = document.getElementById("star_rating_3");
const starRating4 = document.getElementById("star_rating_4");
const starRating5 = document.getElementById("star_rating_5");
const stars = [starRating1, starRating2, starRating3, starRating4, starRating5];

stars.forEach((star, index) => {
    star.addEventListener("click", () => {
        // Reset all stars (remove active class)
        stars.forEach(s => s.classList.remove("active"));
        // Activate stars up to the clicked one
        for (let i = 0; i <= index; i++) {
            stars[i].classList.add("active");
        }
        document.getElementById("selected_rating").value = index + 1;
    });
});
//---