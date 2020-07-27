const fa = document.getElementById("fa");
const eng = document.getElementById("eng");
const navitems = document.getElementsByClassName("navi");

function langch(e) {
  if (e == 0) {
    console.log(12);

    eng.classList.add("activel");
    eng.classList.remove("deal");
    fa.classList.add("deal");
    fa.classList.remove("activel");
  } else if (e == 1) {
    fa.classList.add("activel");
    fa.classList.remove("deal");
    eng.classList.add("deal");
    eng.classList.remove("activel");
  }
}

document.body.onscroll = function () {
  console.log(1);

  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    for (let i = 0; i < navitems.length; i++) {
      navitems[i].classList.add("navrotate");
    }
  } else {
    for (let i = 0; i < navitems.length; i++) {
      navitems[i].classList.remove("navrotate");
    }
  }
};
