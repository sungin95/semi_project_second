// $("#test1").click(function(){
// 	$('#first').show();
//   $('#second').hide();
//   $('#third').hide();
// });

// $("#test2").click(function(){
// 	$('#second').show();
//   $('#first').hide();
//   $('#third').hide();
// });

// $("#test3").click(function(){
// 	$('#third').show();
//   $('#first').hide();
//   $('#second').hide();
// });

// $(function() {
//   $("#test1").on("click", function() {
//       $("#fist").slideUp();
//       $('#second').hide();
//       $('#third').hide();
//   });
  
//   $("#test2").on("click", function() {
//     $("#fist").hide();
//     $('#second').slideUp();
//     $('#third').hide();
//   });
//   $("#test3").on("click", function() {
//     $("#fist").hide();
//     $('#second').hide();
//     $('#third').slideUp();
//   });
// });



$(function() {
  $("#test1").on("click", function() {
      $("#first").show();
  })
  $("#test1").on("click", function() {
      $("#second").hide();
  })
})

$(function() {
  $("#test1").on("click", function() {
      $("#first").show();
  })
  $("#test1").on("click", function() {
      $("#third").hide();
  })
})


$(function() {
  $("#test2").on("click", function() {
      $("#second").show();
  })
  $("#test2").on("click", function() {
      $("#first").hide();
  })
})

$(function() {
  $("#test2").on("click", function() {
      $("#second").show();
  })
  $("#test2").on("click", function() {
      $("#third").hide();
  })
})


$(function() {
  $("#test3").on("click", function() {
      $("#third").show();
  })
  $("#test3").on("click", function() {
      $("#second").hide();
  })
})

$(function() {
  $("#test3").on("click", function() {
      $("#third").show();
  })
  $("#test3").on("click", function() {
      $("#first").hide();
  })
})


$(document).ready(function(){
  $("#test1").trigger('click'); 
});



var focused = null;
$(".test1").focus(function () {
    focused = $(this);
});

