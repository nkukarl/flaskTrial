$(function() {
   $('button#show').bind('click', function () {
       $.getJSON($SCRIPT_ROOT + '/_info', {
       }, function(table_info) {
           render_table(table_info);
       });
       return false;
   });
});

obj_to_arr = (obj) => {
    return Object.keys(obj).map(
        function (key) {
            return obj[key];
        }
    );
};

render_table = (table_info) => {
    // Convert data into correct format
    data = [];
    table_info.data.forEach((dt) => {
        data.push(obj_to_arr(dt));
    });
    // Generate table
    $('#holding_info').DataTable({
        data,
        columns: [
            { title: "Code" },
            { title: "Exchange" },
            { title: "Price" },
            { title: "Volume" },
        ],
    });
    // Diable show button
    $('#show').attr('disabled', true);
};