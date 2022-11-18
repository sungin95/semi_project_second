const arrTop = ["display", "weight", "processor", "graphic", "storage", "price"];
var a;

for (let i = 1; i <= 6; i++) {
    eval(`let plusClick` + i);
    a = document.querySelector(`.plus-click-${arrTop[i - 1]}`);
    a.addEventListener("click", (e) => {
        let hiddenVisible = e.target.parentElement.parentElement.style;
        if (hiddenVisible.overflow == "hidden") {
            hiddenVisible.overflow = "visible";
            hiddenVisible.height = "100%";
        } else {
            hiddenVisible.overflow = "hidden";
            hiddenVisible.height = "45px";
        }
    });
}

const arrBottom = ["size", "resolution", "AMD", "intel", "apple", "external"];

for (let j = 1; j <= 6; j++) {
    eval(`let plusClick` + j);
    b = document.querySelector(`.plus-click-${arrBottom[j - 1]}`);
    b.addEventListener("click", (e) => {
        let hiddenVisible2 = e.target.parentElement.parentElement.style;
        if (hiddenVisible2.overflow == "hidden") {
            hiddenVisible2.overflow = "visible";
            hiddenVisible2.height = "100%";
        } else {
            hiddenVisible2.overflow = "hidden";
            hiddenVisible2.height = "25px";
        }
    });
}
