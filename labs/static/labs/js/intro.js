//네비게이션바 투명
const main = document.querySelector("main");
window.addEventListener("load", () => {
    main.style.minHeight = "0";
});
const introNabvar = document.querySelector("#navbar");
window.addEventListener("load", () => {
    introNabvar.style.backgroundImage = "none";
});
window.addEventListener("scroll", () => {
    if (window.scrollY < 200) {
        navbar.style.transform = "translateY(0%)";
    }
});
introNabvar.addEventListener("mouseleave", () => {
    introNabvar.style.backgroundImage = "none";
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
        if (k.className == "show") {
            continue;
        } else {
            k.classList.remove("show");
        }
    }
    introCommentChange[i % count].classList.add("show");
    i++;
}, 3300);

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
const scrollEventValue = document.querySelector(".intro-value-wrapper");

window.addEventListener("scroll", () => {
    if (window.scrollY > 330) {
        scrollEventValue.style.transform = "translateX(0%)";
        scrollEventValue.style.visibility = "visible";
        scrollEventValue.style.opacity = "1";
    }
    if (window.scrollY > 1500) {
        scrollEventValue.style.transform = "translateX(10%)";
        scrollEventValue.style.visibility = "hidden";
        scrollEventValue.style.opacity = "0";
    }
    if (window.scrollY < 330) {
        scrollEventValue.style.transform = "translateX(10%)";
        scrollEventValue.style.visibility = "hidden";
        scrollEventValue.style.opacity = "0";
    }
});

// 모험
const scrollEventSchedul = document.querySelector(".intro-schedule-wrapper");
window.addEventListener("scroll", () => {
    if (window.scrollY > 1200) {
        scrollEventSchedul.style.transform = "translateX(0%)";
        scrollEventSchedul.style.visibility = "visible";
        scrollEventSchedul.style.opacity = "1";
    }
    if (window.scrollY > 2400) {
        scrollEventSchedul.style.transform = "translateX(10%)";
        scrollEventSchedul.style.visibility = "hidden";
        scrollEventSchedul.style.opacity = "0";
    }
    if (window.scrollY < 1200) {
        scrollEventSchedul.style.transform = "translateX(10%)";
        scrollEventSchedul.style.visibility = "hidden";
        scrollEventSchedul.style.opacity = "0";
    }
});
