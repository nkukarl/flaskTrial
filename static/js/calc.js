$(function() {
   $('button#calc').bind('click', function () {
       $.getJSON($SCRIPT_ROOT + '/_calc', {
           a: $('input[name="a"]').val(),
           b: $('input[name="b"]').val()
       }, function(data) {
           debugger;
           $('#result').text(data.ans);
       });
       return false;
   });
});