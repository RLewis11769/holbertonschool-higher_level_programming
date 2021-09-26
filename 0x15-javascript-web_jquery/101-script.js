// Add/remove/clear li element from list - make sure document loaded
$(document).ready(function () {
  // Add li element to list
  $('DIV#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });

  // Remove last li element from list
  $('DIV#remove_item').click(function () {
    $('.my_list li').last().remove();
  });

  // Clear all li elements from list
  $('DIV#clear_list').click(function () {
    $('.my_list').empty();
  });
});
