(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	$(".toggle-password").click(function() {

	  $(this).toggleClass("fa-eye fa-eye-slash");
	  var input = $($(this).attr("toggle"));
	  if (input.attr("type") === "password") {
	    input.attr("type", "text");
	  } else {
	    input.attr("type", "password");
	  }
	});


})(jQuery);


//$(document).ready(function() {
//    $('#btn-start').on('click', function() {
//        console.log('count started')
//
//
//        $.ajax({
//            url: "/start_counting/",
//            method: "POST",
//            success: function() {
//                console.log('start clicked')
//                $('#btn-start').attr('style', 'background-color: green', 'color: #fff');
//                $('#btn_stop').attr('style', 'background-color: #234182', 'color: #fff');
//                /*$('#custom_result').attr('style', 'display: none');*/
//
//                $('#custom_result').hide()
//            }
//        });
//    });
//
//    $('#btn_stop').on('click', function() {
////        console.log('stop clicked')
//        let custom_counter_result = $('#total_count').text()
//
//        $.ajax({
//            url: "/stop_counting",
//            method: "POST",
//            data: {custom_counter_result:custom_counter_result},
//            success: function(data) {
//                console.log('stop clicked')
//
//                $('#btn_stop').attr('style', 'background-color: #f00', 'color: #fff');
//                $('#btn-start').attr('style', 'background-color: #234182', 'color: #fff');
//
//                $('#custom_result').html("<h4 class='total_count' style='display:block'>result: " + custom_counter_result + "</h4>");
//                /*$('#custom_result').attr('style', 'display: block');*/
//                $('#custom_result').show()
//            }
//        });
//
//
//    });
//
//});



