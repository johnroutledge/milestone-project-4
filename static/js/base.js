// Sticky Nav after scroll credit: Julio Codes YouTube channel
var height = $('#delivery-banner').height();

$(window).scroll(function () { 
  if ($(window).scrollTop() > 30) {
    $('.nav-bar').addClass('navbar-fixed-top');
  }else {
    $('.nav-bar').removeClass('navbar-fixed-top');
  }
});
