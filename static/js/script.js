$(function(){
	"use strict";
	//slider
	$('.owl').each( function() {
		var $carousel = $(this);
		$carousel.owlCarousel({
			items : $carousel.attr('data-items'),
			itemsDesktop : [1199,$carousel.attr('data-itemsDesktop')],
			itemsDesktopSmall : [979,$carousel.attr('data-itemsDesktopSmall')],
			itemsTablet:  [797,$carousel.attr('data-itemsTablet')],
			itemsMobile :  [479,$carousel.attr('data-itemsMobile')],
			navigation : true,
			pagination: true
		});
	});
	//zoom image
	$('.image-zoom').magnificPopup({
		type:'image'
	});
	//loading
	$(window).load(function()
	{
		$('.preloader p').fadeOut();
		$('.preloader').delay(500).fadeOut('slow');
		$('body').delay(600).css({'overflow':'visible'});
	});
	//menu
	function height_w(){
		$('.nav').css('max-height',$(window).height()-70);
	}
	$('.navbar-toggle').click(function(){
		height_w();
	});
	window.onresize = function(){
		height_w();
	};
});