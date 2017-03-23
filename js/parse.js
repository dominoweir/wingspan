function parseSubmission(){
    var formString = $('#form').serialize();
    var betterString = formString.replace(/&/g,"=");
    var formArray = betterString.split("=");
    runPyScript(formArray);
}
function runPyScript(input){
  $.ajax({
    type: "POST",
    url: "../python/getTime.py",
    data: { param: input}
    })
}
