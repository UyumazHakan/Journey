$(document).ready(function(){
	resize_profile_picture();
	$(window).resize(function(){
		resize_profile_picture();
	});
	
});

var resize_profile_picture = function(){
	var cw = Math.min($('.detailed.picture').width(), 170);
$('.detailed.picture').css({
    'height': cw + 'px','margin-top':-(cw-20)+'px'
});
}