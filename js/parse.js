function parseSubmission(){
    var formString = $('#form').serialize();
    var betterString = formString.replace(/&/g,"=");
    var formArray = betterString.split("=");
    return formArray;
}
