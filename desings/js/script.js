$(document).ready(function () {
    resize_profile_picture();
    $(window).resize(function () {
        resize_profile_picture();
    });

});

var resize_profile_picture = function () {
    var detailed_picture = $('.detailed.picture');
    var cw = Math.min(detailed_picture.width(), 170);
    detailed_picture.css({
        'height': cw + 'px', 'margin-top': -(cw - 20) + 'px'
    });
};