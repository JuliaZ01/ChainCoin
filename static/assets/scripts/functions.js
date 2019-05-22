
/* ---------------------------------------------------------------------------
 * Navigation Sub Arrow Function
 * --------------------------------------------------------------------------- */
	jQuery(document).ready(function($) {
		jQuery(".sub-dropdown").parent("li").addClass("parentIcon");
	});
	
	/* ---------------------------------------------------------------------------
	  * Counter Integers Function
	  * --------------------------------------------------------------------------- */
	  jQuery(document).ready(function( $ ) {
		  if($('.custom-counter').length != ''){
			  $('.custom-counter').counterUp({
				  delay: 10,
				  time: 1000
			  });
		  }
	  });
	  
	 /* ---------------------------------------------------------------------------
   * Skills Function
   * --------------------------------------------------------------------------- */
    jQuery(document).ready(function(){
      jQuery('.skillbar').each(function() {
          jQuery(this).find('.skillbar-bar').animate({
            width: jQuery(this).attr('data-percent')
          }, 2000);
        }, {
          offset: "100%",
          triggerOnce: true
        });
      });

if($('#countdown').length != ''){
	jQuery(function () {
			var austDay = new Date();
			austDay = new Date(austDay.getFullYear() + 1, 1 - 1, 26);
			jQuery('#countdown').countdown({
				until: austDay,
				 format: 'wdhms',
				layout:
				'<div class="main-digit-wrapp"><span class="digit-wrapp"><span class="cs-digit">{d10}</span><span class="cs-digit">{d1}</span></span><span class="countdown-period">days</span></div>' +
				'<div class="main-digit-wrapp has-bg2"><span class="digit-wrapp"><span class="cs-digit">{h10}</span><span class="cs-digit">{h1}</span></span><span class="countdown-period">hours</span></div>' +
				'<div class="main-digit-wrapp has-bg3"><span class="digit-wrapp"><span class="cs-digit">{m10}</span><span class="cs-digit">{m1}</span></span><span class="countdown-period">minutes</span></div>' +
				'<div class="main-digit-wrapp has-bg4"><span class="digit-wrapp"><span class="cs-digit">{s10}</span><span class="cs-digit">{s1}</span></span><span class="countdown-period">seconds</span></div>' 
			});
		});
}