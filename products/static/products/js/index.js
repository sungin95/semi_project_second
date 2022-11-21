// 사이드바 여닫이
const arrTop = ["display", "weight", "processor", "graphic", "storage", "price", "brand"];
var a;
for (let i = 1; i <= arrTop.length; i++) {
    eval(`let plusClick` + i);
    a = document.querySelector(`.plus-click-${arrTop[i - 1]}`);
    a.addEventListener("click", (e) => {
        let hiddenVisible = e.target.parentElement.parentElement.style;
        if (hiddenVisible.overflow == "hidden") {
            hiddenVisible.overflow = "visible";
            hiddenVisible.height = "100%";
            e.target.classList.add("bi-dash");
            e.target.classList.remove("bi-plus");
        } else {
            hiddenVisible.overflow = "hidden";
            hiddenVisible.height = "45px";
            e.target.classList.add("bi-plus");
            e.target.classList.remove("bi-dash");
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
            e.target.classList.add("bi-dash");
            e.target.classList.remove("bi-plus");
        } else {
            hiddenVisible2.overflow = "hidden";
            hiddenVisible2.height = "30px";
            e.target.classList.add("bi-plus");
            e.target.classList.remove("bi-dash");
        }
    });
}

// 스크롤시 네비게이션바 숨기기
window.addEventListener("mousewheel", (e) => {
    const direction = e.deltaY > 0 ? "Scroll Down" : "Scroll Up";
    if (direction == "Scroll Down") {
        navbar.style.transform = "translateY(-100%)";
    } else {
        navbar.style.transform = "translateY(0%)";
    }
});

// 클릭 제한
window.onkeydown = function (event) {
    var kcode = event.keyCode;
    if (kcode == 116) {
        history.replaceState({}, null, location.pathname);
    }
};

// 리셋버튼
document.querySelector("#resetBtn").addEventListener("click", () => {
    document.querySelectorAll(".input-tag").forEach(function (ch) {
        ch.checked = false;
    });
});

// 다중 클릭금지
function NoMultiChkBrand(chk) {
    var obj = document.getElementsByName("brand");
    for (var i = 0; i < obj.length; i++) {
        if (obj[i] != chk) {
            obj[i].checked = false;
        }
    }
}

function NoMultiChkSize(chk) {
    var obj = document.getElementsByName("size");
    for (var i = 0; i < obj.length; i++) {
        if (obj[i] != chk) {
            obj[i].checked = false;
        }
    }
}

function NoMultiChkResolution(chk) {
    var obj = document.getElementsByName("resolution");
    for (var i = 0; i < obj.length; i++) {
        if (obj[i] != chk) {
            obj[i].checked = false;
        }
    }
}

function NoMultiChkWeight(chk) {
    var obj = document.getElementsByName("weight");
    for (var i = 0; i < obj.length; i++) {
        if (obj[i] != chk) {
            obj[i].checked = false;
        }
    }
}

var objProcessor = document.getElementsByName("processor_number");
function NoMultiChkProcessor(chk) {
    var obj = document.getElementsByName("processor");
    for (var i = 0; i < obj.length; i++) {
        if (obj[i] != chk) {
            obj[i].checked = false;
        }
    }
    objProcessor.forEach((ch) => {
        ch.checked = false;
    });
}

var objProcessorA = document.getElementsByName("processor");
function NoMultiChkProcessorNumber(chk) {
    var obj = document.getElementsByName("processor_number");
    for (var i = 0; i < obj.length; i++) {
        if (obj[i] != chk) {
            obj[i].checked = false;
        }
    }
    objProcessorA.forEach((ch) => {
        ch.checked = false;
    });
}

function NoMultiChkGraphic(chk) {
    var obj = document.getElementsByName("graphic");
    for (var i = 0; i < obj.length; i++) {
        if (obj[i] != chk) {
            obj[i].checked = false;
        }
    }
}

function NoMultiChkStorage(chk) {
    var obj = document.getElementsByName("storage");
    for (var i = 0; i < obj.length; i++) {
        if (obj[i] != chk) {
            obj[i].checked = false;
        }
    }
}

function NoMultiChkPrice(chk) {
    var obj = document.getElementsByName("price");
    for (var i = 0; i < obj.length; i++) {
        if (obj[i] != chk) {
            obj[i].checked = false;
        }
    }
}
