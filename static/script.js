$(document).ready(function (e) {

  if (window.location.hash) {
    scrollToSection(window.location.hash);
  }

});

$('a[href$="home"]').click(function (e) {
  // Tells the browser not to mess with our links or anchor tags
  e.preventDefault();

  // Because we are redefining how it should behave...
  if (this.pathname === window.location.pathname) {
    // ...that is to scroll to a section of the page
    // IF we are on the intended page
    scrollToSection(this.hash);
  }
  else {
    // Otherwise, redirect them to the page
    window.location.replace(this.href);
  }
});

function scrollToSection(id) {
  $('html, body').animate({
    scrollTop: $(id).offset().top
  }, 1000);
}