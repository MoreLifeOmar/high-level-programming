// JQuery
$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  $('div#character').text(data.name);
});
