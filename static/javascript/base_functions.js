// Alerts the user when no objects are found...
// TODO: Validation and error checking...
function noObjectsPresent(objectClass) {
    alert("There were no, " + objectClass + "'s found!");
}


// DEV: Display number of elements found...
// TODO: Validation and error checking...
function numberOfObjects(objectClass) {
    alert ("There were, " + objectClass + " records found.");
}


// Makes sure the user wishes to delete the pack...
// TODO: Validation and error checking...
function checkDelete(event) {
    var answer = confirm("Are you sure you wish to delete this workpack? This process cannot be undone");
    if (answer == true) {
        alert("Work pack deleted successfully.");
    }
    else {
        event.preventDefault();
    }
}

// Checks weather the user wishes to enter a another set of base estimates...
// TODO: Validation and error checking...
function checkMoreEstimates() {
    var answer = confirm('Would you line to enter another set of estimates?');
    if (answer == true) {
        var postURL = "http://localhost:8000/new-estimates/";
        $.post(postURL, {answer: answer}, function(response) {
            alert(response);
        })
    }
}