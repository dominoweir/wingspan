pl.view.createFlight = {
  setupUserInterface: function () {
    var saveButton = document.forms['basic'].commit;
    // load all flight objects
    Flight.loadAll();
    // Set an event handler for the save/submit button
    saveButton.addEventListener("click",
        pl.view.createFlight.handleSaveButtonClickEvent);
    window.addEventListener("beforeunload", function () {
        Flight.saveAll();
    });
  },
  handleSaveButtonClickEvent: function () {
    var formEl = document.forms['basic'];
    var slots = { isbn: formEl.isbn.value,
        title: formEl.title.value,
        year: formEl.year.value};
    Flight.add(slots);
    formEl.reset();
  }
};
