const ham = document.getElementById("ham");

// if (window.innerWidth < 460) {
//   document.getElementById(
//     "sc"
//   ).innerHTML = `                <div class="mySlides fade">
//   <img src="./static/m-front-fa.png" style="width:100%">
// </div>

// <div class="mySlides fade">
//   <img src="./static/m-back-fa.png" style="width:100%">
// </div>

// <div class="mySlides fade">
//   <img src="./static/m-ui-fa.png" style="width:100%">
// </div>
// `;
// }
// slider
var slideIndex = 0;
window.onresize = function () {
  if (window.innerWidth > 1080) {
    closeNav();
  }
};
// navbar s

window.onscroll = function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("mon").style.height = "6vh";
    document.getElementById("logo").style.fontSize = "38px";
  } else {
    document.getElementById("mon").style.height = "10vh";
    document.getElementById("logo").style.fontSize = "48px";
  }
};

function mobileNav(e) {
  ham.classList.toggle("fa-bars");
  ham.classList.toggle("fa-close");
  if (e == "fa") {
    document.getElementById("links").classList.toggle("m-links-show");
  } else if (e == "en") {
    document.getElementById("links").classList.toggle("m-links-show-en");
  }
}

function closeNav() {
  ham.classList.add("fa-bars");
  ham.classList.remove("fa-close");
  document.getElementById("links").classList.remove("m-links-show");
  document.getElementById("links").classList.remove("m-links-show-en");
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("loaderoff").style.display = "block";
}

// navbar end

// function theme() {
//   document.getElementById("cssfile").href = `{% static "portfolio/dark.css" %}`;
//   console.log("working");
//   return false
// }

showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
  setTimeout(showSlides, 3200); // Change image every 2 seconds
}
