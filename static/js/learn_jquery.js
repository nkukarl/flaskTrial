$(document).ready(
    function() {
        $('#section_0').html('Hello world!');

        $('#section_1').find('p').css('background-color', 'yellow');

        $('#section_2').find('li:even').css('font-size', '12px');
        $('#section_2').find('li:odd').css('font-size', '16px');
        $('#section_2').find('li:lt(3)').css('background-color', 'blue');
    }
);