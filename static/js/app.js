window.onload = function () {
  loadElements();
  console.log("window loaded");
};

const loadElements = async () => {
  const delay = (ms) => new Promise((res) => setTimeout(res, ms));

  const slideIn = document.querySelector(".slide-in-bottom");
  slideIn.classList.add("active");
  console.log("slide-in class added");

  const slideRight = document.querySelector(".slide-in-right");
  slideRight.classList.add("active");

  await delay(100);

  const dropTop = document.querySelector(".drop-from-top");
  dropTop.classList.add("active");
};

function flipped_empathy() {
  console.log("hovered");
}
