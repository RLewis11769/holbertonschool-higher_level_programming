// Add '<li>Item</li>' to ul.my_list on click DIV#add_item
$('DIV#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
