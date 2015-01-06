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


$(document).ready(function() {
   $('.workpacklinks').click(function(event) {
       event.preventDefault();
       $.ajax({
           url: '/home/',
           type: 'POST',
           datatype: 'json',
           data: {
               csrfmiddlewaretoken: "{{ csrf_token }}",
               workpacknumber: $('#wpnum').html()
           },
           success: function(data) {
               $('#worknumber').html($('#wpnum').html());

           }
       });
   });
});


$(function() {
  $( "#addPrefabDialog" ).dialog({
      autoOpen: false,
      buttons: {
          CANCEL: function() {
              $(this).dialog("close");
          },
          SAVE: function() {
              var lineclass = $('#Combobox1').val();
              var itemname = $('#Combobox2').val();
              var diameter = $('#Combobox3').val();
              var quantity = $('#Combobox4').val();

              $.ajax({
                 url: '/home/',
                 type: 'POST',
                 data: {
                    csrfmiddlewaretoken: "{{ csrf_token }}",
                    lineclass: lineclass,
                    itemname: itemname,
                    diameter: diameter,
                    quantity: quantity,
                    name: 'Prefab'
                 },
                 success: function(data) {
                    $('#prefablineclass').html(lineclass);
                    $('#prefabname').html(itemname);
                    $('#prefabdiameter').html(diameter);
                    $('#prefabquantity').html(quantity);
                    $(this).dialog("close");
                 },
                 failure: function(data) {
                    alert('The post could not happen.');
                 }
              });
          }},
      height: 230,

      title: "Enter Prefab Item",
      position: {
          my: "center",
          at: "center"
      }
  });

  $( "#jQueryButton1" ).click(function() {
     $( "#addPrefabDialog" ).dialog( "open" );
     $('#Combobox1').on('change', function() {
         var lineclass = $(this).val();
         $.ajax({
             url: '/home/',
             type: 'POST',
             data: {
                 csrfmiddlewaretoken: "{{ csrf_token }}",
                 lineclass: lineclass
             },
             success: function(data) {

             },
             failure: function(data) {

             }
         })
     });
  });
});
