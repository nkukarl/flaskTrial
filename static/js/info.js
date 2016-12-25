$(function() {
   $('button#show').bind('click', function () {
       $.getJSON($SCRIPT_ROOT + '/_info', {
       }, function(table_info) {
           render_table(table_info);
       });
       return false;
   });
});

render_table = (table_info) => {

    let table = document.getElementById('table');
    while (table.firstChild) {
        table.removeChild(table.firstChild);
    }

    const data = table_info.data;

    if (data[0]) {
        let keys = Object.keys(data[0]);

        let el = document.createDocumentFragment();

        const title = table_info.title;
        const caption = document.createElement('caption');
        caption.appendChild(document.createTextNode(title));

        el.appendChild(caption);

        let header = document.createElement('tr');
        let hidden_button = document.createElement('button');
        hidden_button.className = 'hidden';
        header.appendChild(hidden_button);
        keys.forEach((key) => {
            let cell = document.createElement('th');
            cell.appendChild(document.createTextNode(key));
            header.appendChild(cell);
        });

        el.appendChild(header);

        for (let i = 0; i < data.length; i++) {
            let dt = data[i];
            let row = document.createElement('tr');
            row.id = 'holding_details_row_' + i.toString();
            del_button = document.createElement('button');
            del_button.innerHTML = 'Remove';
            del_button.className = 'del_btn';
            row.appendChild(del_button);

            keys.forEach((key) => {
                let cell = document.createElement('td');
                cell.className = key;
                cell.appendChild(document.createTextNode(dt[key]));
                row.appendChild(cell)
            });

            el.appendChild(row);
        }
        document.getElementById('table').appendChild(el);
    } else {
        document.getElementById('table').appendChild(document.createTextNode('No holding info!'));
    }
};