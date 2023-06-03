window.addEventListener("scroll", function () {
    var nav = document.querySelector("#mainNavbar");
    nav.classList.toggle("sticky", window.scrollY > 0)
});



var BtnCanvas = document.querySelectorAll(".btn-close-canvas");
for (let i = 0; i < BtnCanvas.length; i++) {
    BtnCanvas[i].addEventListener("click", function(){
        document.querySelector('[data-bs-dismiss="offcanvas"]').click();
    });
}

