//네비게이션바 투명
const main = document.querySelector("main");
window.addEventListener("load", () => {
    main.style.minHeight = "0";
});
const introNabvar = document.querySelector("#nabvar");
window.addEventListener("load", () => {
    introNabvar.style.backgroundColor = "transparent";
});
window.addEventListener("scroll", () => {
    if (window.scrollY == 0) {
        introNabvar.style.backgroundColor = "transparent";
    }
});
introNabvar.addEventListener("mouseleave", () => {
    introNabvar.style.backgroundColor = "transparent";
});

//글귀변경
const introCommentChangeH3 = document.querySelector(".intro-comment-change h3");
const introCommentChangeP = document.querySelector(".intro-comment-change p");
const introCommentChange = document.querySelectorAll(".intro-comment-change");
const count = introCommentChange.length;
var i = 0;

var time;
// 멘트
let time_set = setInterval(() => {
    for (let k of introCommentChange) {
        k.classList.remove("show");
    }
    introCommentChange[i % count].classList.add("show");
    i++;
}, 3000);

// 멘트 클릭 이벤트
for (let rel of introCommentChange) {
    rel.addEventListener("click", () => {
        clearInterval(time);
        for (let re of introCommentChange) {
            re.classList.remove("show");
        }
        introCommentChange[i % count].classList.add("show");
        i++;
    });
}

// 스크롤 이벤트
// 규칙
window.addEventListener("scroll", () => {
    if (window.scrollY > 330) {
        document.querySelector(".intro-value-wrapper").style.transform = "translateX(0%)";
        document.querySelector(".intro-value-wrapper").style.visibility = "visible";
        document.querySelector(".intro-value-wrapper").style.opacity = "1";
    }
    if (window.scrollY > 1500) {
        document.querySelector(".intro-value-wrapper").style.transform = "translateX(10%)";
        document.querySelector(".intro-value-wrapper").style.visibility = "hidden";
        document.querySelector(".intro-value-wrapper").style.opacity = "0";
    }
    if (window.scrollY < 330) {
        document.querySelector(".intro-value-wrapper").style.transform = "translateX(10%)";
        document.querySelector(".intro-value-wrapper").style.visibility = "hidden";
        document.querySelector(".intro-value-wrapper").style.opacity = "0";
    }
});

// 모험
window.addEventListener("scroll", () => {
    if (window.scrollY > 1200) {
        document.querySelector(".intro-schedule-wrapper").style.transform = "translateX(0%)";
        document.querySelector(".intro-schedule-wrapper").style.visibility = "visible";
        document.querySelector(".intro-schedule-wrapper").style.opacity = "1";
    }
    if (window.scrollY > 2400) {
        document.querySelector(".intro-schedule-wrapper").style.transform = "translateX(10%)";
        document.querySelector(".intro-schedule-wrapper").style.visibility = "hidden";
        document.querySelector(".intro-schedule-wrapper").style.opacity = "0";
    }
    if (window.scrollY < 1200) {
        document.querySelector(".intro-schedule-wrapper").style.transform = "translateX(10%)";
        document.querySelector(".intro-schedule-wrapper").style.visibility = "hidden";
        document.querySelector(".intro-schedule-wrapper").style.opacity = "0";
    }
});
