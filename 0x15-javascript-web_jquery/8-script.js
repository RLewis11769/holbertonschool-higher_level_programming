// Get title of ul#list_movies from api (multiple in li)
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const title in data.results) {
    $('ul#list_movies').append('<li>' + data.results[title].title + '</li>');
  }
});
