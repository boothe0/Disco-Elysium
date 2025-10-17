const kimImagesAndLinks = [
  {
    name: "kim1",
    src: "static/images/kim1.jpg",
    link: "https://www.pinterest.com/pin/862157922457429852",
  },
  {
    name: "kim2",
    src: "static/images/kim2.jpg",
    link: "https://www.pinterest.com/pin/703756187759018",
  },
  {
    name: "kim3",
    src: "static/images/kim3.jpg",
    link: "https://www.pinterest.com/pin/7388786884168824",
  },
  {
    name: "kim4",
    src: "static/images/kim4.jpg",
    link: "https://www.pinterest.com/pin/7388786884168820",
  },
  {
    name: "kim5",
    src: "static/images/kim5.jpg",
    link: "https://www.pinterest.com/pin/16114511159831608",
  },
];
const harryImagesAndLinks = [
  {
    name: "harry1",
    src: "static/images/harry1.jpg",
    link: "https://www.pinterest.com/pin/862157922457429985/",
  },
  {
    name: "harry2",
    src: "static/images/harry2.jpg",
    link: "https://www.pinterest.com/pin/862157922457429853/",
  },
  {
    name: "harry3",
    src: "static/images/harry3.jpg",
    link: "https://www.pinterest.com/pin/862157922457429838/",
  },
  {
    name: "harry4",
    src: "static/images/harry4.jpg",
    link: "https://www.pinterest.com/pin/862157922452462049/",
  },
  {
    name: "harry5",
    src: "static/images/harry5.jpg",
    link: "https://www.pinterest.com/pin/862157922452462088/",
  },
];
function rotateImages() {
  pictureArray = document.querySelectorAll(".rotating-pic");

  if (pictureArray[0].classList.contains("kim")) {
    pictureArray.forEach((pic, i) => {
      pic.src = harryImagesAndLinks[i]["src"];
      document.getElementById(`artist-credits${i}`).href =
        harryImagesAndLinks[i]["link"];

      pic.classList.add("harry");
      pic.classList.remove("kim");
      pic.classList.add("fade-in-rotating-pic");
    });
  } else {
    pictureArray.forEach((pic, i) => {
      pic.src = kimImagesAndLinks[i]["src"];
      document.getElementById(`artist-credits${i}`).href =
        kimImagesAndLinks[i]["link"];
      pic.classList.add("kim");
      pic.classList.remove("harry");
      pic.classList.add("fade-in-rotating-pic");
    });
  }
  setTimeout(() => {
    document.querySelectorAll(".rotating-pic").forEach((pic) => {
      pic.classList.remove("fade-in-rotating-pic");
    });
  }, 1000);
}
rotateImages();
// needs to be multiple the timeout of the fade in class removal to allow for time
setInterval(rotateImages, 12000);
