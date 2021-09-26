// Toggles between red and green class on click DIV#toggle_header
$('DIV#toggle_header').click(function () {
  if ($("header").hasClass("red")) {
    $("header").toggleClass("green");
  } else {
    $("header").toggleClass("red");
  }
});
