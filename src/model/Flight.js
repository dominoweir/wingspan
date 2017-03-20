// https://www.codeproject.com/Articles/753724/JavaScript-Front-End-Web-App-Tutorial-Part

function Flight( slots) {
  this.isbn = slots.isbn;
  this.title = slots.title;
  this.year = slots.year;
};

Flight.loadAll = function () {
  var i=0, key="", keys=[], flightTableString="", flightTable={};
  try {
    if (localStorage["flightTable"]) {
      flightTableString = localStorage["flightTable"];
    }
  } catch (e) {
    alert("Error when reading from Local Storage\n" + e);
  }
  if (flightTableString) {
    flightTable = JSON.parse( flightTableString);
    keys = Object.keys( flightTable);
    console.log( keys.length +" flights loaded.");
    for (i=0; i < keys.length; i++) {
      key = keys[i];
      Flight.instances[key] = Flight.convertRow2Obj( flightTable[key]);
    }
  }
};

Flight.saveAll = function () {
  var flightTableString="", error=false,
      nmrOfFlights = Object.keys( Flight.instances).length;
  try {
    flightTableString = JSON.stringify( Flight.instances);
    localStorage["flightTable"] = flightTableString;
  } catch (e) {
    alert("Error when writing to Local Storage\n" + e);
    error = true;
  }
  if (!error) console.log( nmrOfFlights + " flights saved.");
};

Flight.add = function (slots) {
  var flight = new Flight( slots);
  Flight.instances[slots.isbn] = flight;
  console.log("Flight " + slots.isbn + " created!");
};

Flight.update = function (slots) {
  var flight = Flight.instances[slots.isbn];
  var year = parseInt( slots.year);
  if (flight.title !== slots.title) { flight.title = slots.title;}
  if (flight.year !== year) { flight.year = year;}
  console.log("Flight " + slots.isbn + " modified!");
};

Flight.destroy = function (isbn) {
  if (Flight.instances[isbn]) {
    console.log("Flight " + isbn + " deleted");
    delete Flight.instances[isbn];
  } else {
    console.log("There is no flight with ISBN " + isbn + " in the database!");
  }
};

Flight.createTestData = function () {
  Flight.instances["006251587X"] = new Flight({isbn:"006251587X", title:"Weaving the Web", year:2000});
  Flight.instances["0465026567"] = new Flight({isbn:"0465026567", title:"Gödel, Escher, Bach", year:1999});
  Flight.instances["0465030793"] = new Flight({isbn:"0465030793", title:"I Am A Strange Loop", year:2008});
  Flight.saveAll();
};

Flight.clearData = function () {
  if (confirm("Do you really want to delete all flight data?")) {
    localStorage["flightTable"] = "{}";
  }
};
