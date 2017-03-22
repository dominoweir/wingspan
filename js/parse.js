function parseSubmission(){
    var formData = document.getElementById("form");
    var text = "";
    var i;
    for (i = 0; i < x.length ;i++) {
        text += x.elements[i].value + "<br>";
    }
    runPyScript(text);
}
function runPyScript(input){
  $.ajax({
    type: "POST",
    url: "../python/getTime.py",
    data: { param: input},
    }).done(function( o ) {
    alert("OK");
  });
}
