document.addEventListener("DOMContentLoaded", function() {
    window.addEventListener("scroll", function () {
        var nav = document.querySelector("#mainNavbar");
        nav.classList.toggle("sticky", window.scrollY > 0)
    });
    checkDevice();
});



//scroll-up
let calcScrollValue = () =>{
    let scrollProgress = document.getElementById("progress");
    let progressValue = document.getElementById("progress-value");
    let pos = document.documentElement.scrollTop;
    let calcHeight = 
        document.documentElement.scrollHeight -
        document.documentElement.clientHeight;
    let scrollValue = Math.round((pos * 100) / calcHeight);

    if(pos > 150 && window.innerWidth < 767){
        scrollProgress.style.display = "none";
        progressValue.style.display = "none";
    }
    else if(pos > 150 && window.innerWidth > 767){
        scrollProgress.style.display = "grid";
        progressValue.style.display = "grid";
    }
    else{
        scrollProgress.style.display = "none";
        progressValue.style.display = "none";
    }

    scrollProgress.addEventListener("click", () => {
        document.documentElement.scrollTop = 0;
    });

    scrollProgress.style.background = 
    `conic-gradient(#262323 ${scrollValue}%, #aaaaaa ${scrollValue}% )`;
}

window.onscroll = calcScrollValue;
window.onload = calcScrollValue;




//Kullanıcının mobil cihaz ile girip girmediğini kontrol ediyoruz.
function checkDevice(){
    var isMobile = window.matchMedia("(max-width: 768px)").matches;
      
    //Kullanıcı mobil cihaz ile girmişse bu kod bloğu çalışacak.
    var links = document.querySelectorAll(".navbar-nav .nav-link");
    if (isMobile) {
        links.forEach(function(link) {
            if(link.classList.contains("effect")){
                link.classList.remove("effect");
            }
        })
    } else{
        links.forEach(function(link) {
            if(!link.classList.contains("effect")){
                link.classList.add("effect");
            }
        })
    }
}



var BtnCanvas = document.querySelectorAll(".btn-close-canvas");
for (let i = 0; i < BtnCanvas.length; i++) {
    BtnCanvas[i].addEventListener("click", function(){
        document.querySelector('[data-bs-dismiss="offcanvas"]').click();
    });
}



function checkScreenWidthForAnimation(){
    var element = document.querySelector(".my");
    if (window.innerWidth > 767){
        if (!element.classList.contains("anim-typewriter")) {    
            element.classList.add("anim-typewriter");
            element.classList.remove("anim-typewriter-small");
            element.classList.remove("anim-typewriter-xsmall");
            element.classList.remove("anim-typewriter-xxsmall");
        }
    }
    else if(window.innerWidth > 576 && window.innerWidth <= 767){
        if (!element.classList.contains("anim-typewriter-small")) {    
            element.classList.add("anim-typewriter-small");
            element.classList.remove("anim-typewriter");
            element.classList.remove("anim-typewriter-xsmall");
            element.classList.remove("anim-typewriter-xxsmall");
        }
    }
    else if(window.innerWidth > 405 && window.innerWidth <= 576){
        if (!element.classList.contains("anim-typewriter-xsmall")) {    
            element.classList.add("anim-typewriter-xsmall");
            element.classList.remove("anim-typewriter");
            element.classList.remove("anim-typewriter-small");
            element.classList.remove("anim-typewriter-xxsmall");
        }
    }
    else if(window.innerWidth <= 405){
        if (!element.classList.contains("anim-typewriter-xxsmall")) {    
            element.classList.add("anim-typewriter-xxsmall");
            element.classList.remove("anim-typewriter");
            element.classList.remove("anim-typewriter-small");
            element.classList.remove("anim-typewriter-xsmall");
        }
    }
}
checkScreenWidthForAnimation();



function checkScreenWidthForClient(){
    var element = document.documentElement;
    if(window.innerWidth < 991.98){
        if (navigator.userAgent.indexOf("Chrome") != -1) {    
            element.classList.add("chrome-scroll");
        }
    }
    else if (element.classList.contains("chrome-scroll")){
        element.classList.remove("chrome-scroll");
    }
}
checkScreenWidthForClient();



window.addEventListener("resize", function(){
    checkScreenWidthForAnimation();
    checkScreenWidthForClient();
    checkDevice();
});




