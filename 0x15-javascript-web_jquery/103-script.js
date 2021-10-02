// Fetches translation from API based on lang code inputted on click/enter
// API explained/language code examples: https://fourtonfish.com/project/hellosalut-api/

$(document).ready(function () {
  // On button click does 3 things
  $('INPUT#btn_translate').click(function () {
    // 1. Saves url as variable
    const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
    // 2. Saves value of element in input field
    const lang = $('INPUT#language_code').val();
    // 3. Passes concatenated url and lang to get JSON object and calls function on success
    $.getJSON(url + lang, function (data) {
      // JSON object is in format { 'code': 'code', 'hello': 'translation' }
      // JSON object returned is displayed as text in DIV#hello
      $('DIV#hello').text(data.hello);
    });
  });

  // If user presses "enter" in input field, same as button click
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      $('INPUT#btn_translate').click();
    }
  });
});
