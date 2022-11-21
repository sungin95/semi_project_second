$(function () {
    $("#test1").on("click", function () {
        $("#first").show();
    });
    $("#test1").on("click", function () {
        $("#second").hide();
    });
});

$(function () {
    $("#test1").on("click", function () {
        $("#first").show();
    });
    $("#test1").on("click", function () {
        $("#third").hide();
    });
});

$(function () {
    $("#test2").on("click", function () {
        $("#second").show();
    });
    $("#test2").on("click", function () {
        $("#first").hide();
    });
});

$(function () {
    $("#test2").on("click", function () {
        $("#second").show();
    });
    $("#test2").on("click", function () {
        $("#third").hide();
    });
});

$(function () {
    $("#test3").on("click", function () {
        $("#third").show();
    });
    $("#test3").on("click", function () {
        $("#second").hide();
    });
});

$(function () {
    $("#test3").on("click", function () {
        $("#third").show();
    });
    $("#test3").on("click", function () {
        $("#first").hide();
    });
});

$(document).ready(function () {
    $("#test1").trigger("click");
});

var focused = null;
$(".test1").focus(function () {
    focused = $(this);
});
