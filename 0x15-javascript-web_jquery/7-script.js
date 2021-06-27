// Get text of DIV#character name from api
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  const name = data.name;
  $('DIV#character').text(name);
});
