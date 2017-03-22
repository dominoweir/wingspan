function parseSubmission(){
    var formString = $('#form').serialize();
    runPyScript(formString);
}
function runPyScript(input){
  $.ajax({
    type: "POST",
    url: "../python/getTime.py",
    data: { param: input}
    })
}
