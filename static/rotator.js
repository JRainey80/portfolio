const imageContainer = document.querySelector(".image-container");
const prevBtn = document.getElementById("prev");
const nextBtn = document.getElementById("next");

/*console.log(imageContainer);
console.log(prevBtn);
console.log(nextBtn);*/

let x = 0;

prevBtn.addEventListenter("click", () => {
    x = x + 45;
    rotate();
});

nextBtn.addEventListenter("click", () => {
    x = x - 45;
    rotate();
});
function rotate() { 
    imageContainer.style.transform = 'perspective(1000px) rotateY(${x}deg)';
}