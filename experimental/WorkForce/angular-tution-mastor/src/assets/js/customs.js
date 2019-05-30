
jQuery(function() {

	"use strict";
		
		
		
		/**
		 * introLoader - Preloader
		 */
		$("#introLoader").introLoader({
			
			animation: { name: 'gifLoader',
				options: {
					ease: "easeInOutCirc",
					style: 'dark bubble',
					delayBefore: 100,
					delayAfter: 0,
					exitTime: 300,
					onAfter: function(){
						
						var placeholderText = [
							"What do you want to study?",
							"Business?",
							"Computer & IT?",
							"Science?",
							"Design?",
							"Photography?",
							"Writing?"
						];

						$('.placeholder-type-writter').placeholderTypewriter({
							text: placeholderText,
							delay: 70,
						});

						$("#typed").typed({
								stringsElement: $('#typed-strings'),
								typeSpeed: 120,
								backDelay: 900,
								loop: true,
								contentType: 'html',
								showCursor: false,
						});
					},
				},
					
			}
		});	
		
		
		
		/**
		 * Sticky Header
		 */
		$(".container-wrapper").waypoint(function() {
			$(".navbar").toggleClass("navbar-sticky-function");
			$(".navbar").toggleClass("navbar-sticky");
			return false;
		}, { offset: "-20px" });
		
		
		
		/**
		 * Main Menu Slide Down Effect
		 */
		 
		// Mouse-enter dropdown
		$('#navbar li').on("mouseenter", function() {
				$(this).find('ul').first().stop(true, true).delay(350).slideDown(500, 'easeInOutQuad');
		});

		// Mouse-leave dropdown
		$('#navbar li').on("mouseleave", function() {
				$(this).find('ul').first().stop(true, true).delay(100).slideUp(150, 'easeInOutQuad');
		});
		
		
		
		/**
		 * Slicknav - a Mobile Menu
		 */
		var $slicknav_label;
		$('#responsive-menu').slicknav({
			duration: 300,
			easingOpen: 'easeInExpo',
			easingClose: 'easeOutExpo',
			closedSymbol: '<i class="fa fa-plus"></i>',
			openedSymbol: '<i class="fa fa-minus"></i>',
			prependTo: '#slicknav-mobile',
			allowParentLinks: true,
			label:"" 
		});
		
		
		
		/**
		 * Smooth scroll to anchor
		 */
		$('a.anchor[href*=#]:not([href=#])').on("click",function() {
			if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
				var target = $(this.hash);
				target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
				if (target.length) {
					$('html,body').animate({
						scrollTop: (target.offset().top - 70) 
					}, 1000);
					return false;
				}
			}
		});
		
		
		
		/**
		 * Back To Top
		 */
		$(window).scroll(function(){
			if($(window).scrollTop() > 500){
				$("#back-to-top").fadeIn(200);
			} else{
				$("#back-to-top").fadeOut(200);
			}
		});
		$('#back-to-top').on("click",function() {
				$('html, body').animate({ scrollTop:0 }, '800');
				return false;
		});

		
		
		/**
		 * Effect to Bootstrap Dropdown
		 */
		$('.bt-dropdown-click').on('show.bs.dropdown', function(e) {   
			$(this).find('.dropdown-menu').first().stop(true, true).slideDown(500, 'easeInOutQuad'); 
		}); 
		$('.bt-dropdown-click').on('hide.bs.dropdown', function(e) { 
			$(this).find('.dropdown-menu').first().stop(true, true).slideUp(250, 'easeInOutQuad'); 
		});
		
		
		
		/**
		 * Icon Change on Collapse
		 */
		$('.collapse.in').prev('.panel-heading').addClass('active');
		$('.bootstarp-accordion, .bootstarp-toggle').on('show.bs.collapse', function(a) {
			$(a.target).prev('.panel-heading').addClass('active');
		})
		.on('hide.bs.collapse', function(a) {
			$(a.target).prev('.panel-heading').removeClass('active');
		});
		 

		
		/**
		 * Another Bootstrap Toggle
		 */
		$('.another-toggle').each(function(){
			if( $('h4',this).hasClass('active') ){
				$(this).find('.another-toggle-content').show();
			}
		});
		$('.another-toggle h4').on("click",function() {
			if( $(this).hasClass('active') ){
				$(this).removeClass('active');
				$(this).next('.another-toggle-content').slideUp();
			} else {
				$(this).addClass('active');
				$(this).next('.another-toggle-content').slideDown();
			}
		});
		
		

		/**
		 *  Arrow for Menu has sub-menu
		 */
		if ($(window).width() > 992) {
			$(".navbar-arrow > ul > li").has("ul").children("a").append("<i class='arrow-indicator fa fa-angle-down'></i>");
		}
		
		if ($(window).width() > 992) {
			$(".navbar-arrow ul ul > li").has("ul").children("a").append("<i class='arrow-indicator fa fa-angle-right'></i>");
		}

		
		
		/**
		 *  Placeholder
		 */
		$("input, textarea").placeholder();

	
	
		/**
		 *  Bootstrap Tooltip
		 */
		$('[data-toggle="tooltip"]').tooltip()
		
		

		/**
		 * readmore - read more/less
		 */
		$('.read-more-div').readmore({
			speed: 220,
			moreLink: '<a href="#" class="read-more-div-open">Read More</a>',
			lessLink: '<a href="#" class="read-more-div-close">Read less</a>',
			collapsedHeight: 45,
			heightMargin: 25
		});
		
		
		
		/**
		 * Show more-less button
		 */
		$('.btn-more-less').on("click",function(){
			$(this).text(function(i,old){
				return old=='Show more' ?  'Show less' : 'Show more';
			});
		});
		
		
		
		/**
		 * Rang Slider - ionRangeSlider
		 */
		$("#price_range").ionRangeSlider({
			type: "double",
			grid: true,
			min: 0,
			max: 1000,
			from: 200,
			to: 800,
			prefix: "$"
		});
		
		$("#star_range").ionRangeSlider({
			type: "double",
			grid: false,
			from: 1,
			to: 2,
			values: [
				"<i class='fa fa-star'></i>", 
				"<i class='fa fa-star'></i> <i class='fa fa-star'></i>",
				"<i class='fa fa-star'></i> <i class='fa fa-star'></i> <i class='fa fa-star'></i>", 
				"<i class='fa fa-star'></i> <i class='fa fa-star'></i> <i class='fa fa-star'></i> <i class='fa fa-star'></i>",
				"<i class='fa fa-star'></i> <i class='fa fa-star'></i> <i class='fa fa-star'></i> <i class='fa fa-star'></i> <i class='fa fa-star'></i>" 
			]
		});
		
		$("#range_03").ionRangeSlider({
			type: "double",
			grid: true,
			min: 0,
			max: 1000,
			from: 200,
			to: 800,
			prefix: "$"
		});
		
		/**
		 * Bootstrap rating
		 */
		 
		$('.rating-label').rating();
				
		$('.rating-label').each(function () {
			$('<span class="label label-default"></span>')
				.text($(this).val() || ' ')
				.insertAfter(this);
		});
		$('.rating-label').on('change', function () {
			$(this).next('.label').text($(this).val());
		});
		
		
		
		/**
		 * Payment Method
		 */

		$("div.payment-option-form").hide();
		
		$("input[name$='payments']").on("click",function() {
				var test = $(this).val();
				$("div.payment-option-form").hide();
				$("#" + test).show();
		});
		
		
		
		/**
		 * Select 2 - Custom select
		 */
		$(".select2-single").select2({allowClear: true});
		$(".select2-single-no-search").select2({ allowClear: true, minimumResultsForSearch: Infinity});
		$(".select2-multi").select2({});
		
		
		
		/**
		 * Custom Scrollbar - niceScroll
		 */
		 
		$(".nicescroll-module").niceScroll({
			cursorcolor:"#333",
			cursorborder: "none",
			cursorborderradius: "0",
			background: "#EAEAEA",
		});
		
		
		
		/**
		 * Slick Carousel and Slider
		 */
		$('.slick-hero-slider').slick({
			dots: true,
			infinite: true,
			speed: 500,
			slidesToShow: 1,
			slidesToScroll: 1,
			centerMode: true,
			infinite: true,
			centerPadding: '0',
			focusOnSelect: true,
			adaptiveHeight: true,
			autoplay: true,
			autoplaySpeed: 4500,
			pauseOnHover: true,
		});

		
		
		/**
		 * Sign-in and Sign-up modal
		 */
		 
		$.fn.modal.defaults.spinner = $.fn.modalmanager.defaults.spinner = '<div class="loading-spinner" style="width: 60px; margin-left: -30px; margin-top: -30px;>' +
			'<div class="modal-ajax-loading">' +
				'<img src="images/ajax-loading.gif" alt="image" />' +
			'</div>' +
		'</div>';

		var $modal = $('#ajaxLoginModal');

		$(document).on('click', '.btn-ajax-login,.login-box-box-action a' ,function(){
			// create the backdrop and wait for next modal to be triggered
			
			$modalForgotPassword.modal('hide');
			$modalRegister.modal('hide');

			$('body').modalmanager('loading');

			setTimeout(function(){
				 $modal.load('ajax-login-modal-login.html', '', function(){
					$modal.modal();
				});
			}, 1000);
		});

		/** for Register Ajax Modal */

		var $modalRegister = $('#ajaxRegisterModal');

		$(document).on('click', '.btn-ajax-register,.register-box-box-action a' ,function(){

			$modal.modal('hide');
			$modalForgotPassword.modal('hide');

			$('body').modalmanager('loading');

			setTimeout(function(){
				 $modalRegister.load('ajax-login-modal-register.html', '', function(){
					$modalRegister.modal();
				});
			}, 1000);
		});

		/** for Forgot Password Ajax Modal */

		var $modalForgotPassword = $('#ajaxForgotPasswordModal');

		$(document).on('click', '.btn-ajax-forgot-password,.login-box-link-action a' ,function(){

			$modal.modal('hide');
			$modalRegister.modal('hide');

			$('body').modalmanager('loading');

			setTimeout(function(){

				 $modalForgotPassword.load('ajax-login-modal-forgot-password.html', '', function(){
					$modalForgotPassword.modal();
				});

			}, 1000);

		});
		
		

});





