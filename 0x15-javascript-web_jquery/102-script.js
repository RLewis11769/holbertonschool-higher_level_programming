// Fetches translation from API based on lang code inputted on click
// API explained/language code examples: https://fourtonfish.com/project/hellosalut-api/
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    // On button click, saves url as variable
    const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
    // On button click, saves value of element in input field
    const lang = $('INPUT#language_code').val();
    // On button click, passes concatenated url and lang to get JSON object and calls function on success
    $.getJSON(url + lang, function (data) {
      // JSON object is in format { 'code': 'code', 'hello': 'translation' }
      // JSON object returned is displayed as text in DIV#hello
      $('DIV#hello').text(data.hello);
    });
  });
});
