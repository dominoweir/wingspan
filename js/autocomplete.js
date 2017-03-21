function initAutocomplete() {
  var input = document.getElementById('q2');
  var autocomplete = new google.maps.places.Autocomplete(input);
}

google.maps.event.addDomListener(window, 'load', initAutocomplete);
