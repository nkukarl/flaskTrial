$(function() {
   $('button#calc').bind('click', function () {
       $.getJSON($SCRIPT_ROOT + '/_calc', {
           a: $('input[name="a"]').val(),
           b: $('input[name="b"]').val()
       }, function(ans) {
           $('#result').text(ans);
       });
       return false;
   });
});