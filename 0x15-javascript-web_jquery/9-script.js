// Get value of hello from api when imported from head tag
$(document).ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    hello = data.hello;
    $('DIV#hello').text(hello);
  });
});
