function parseSubmission(){
  var formData = new FormData(document.querySelector('basic'));
  var data = formData.entries();
  runPyScript(data);
}
function runPyScript(input){
  $.ajax({
    type: "POST",
    url: "getTime.py",
    data: { param: " "},
    dataType: "text"
    }).done(function( o ) {
    alert("OK");
});

        return jqXHR.responseText;
  }
