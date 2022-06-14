function message_error(obj) {
    console.log(obj);
    var html = '';
    if(typeof (obj) == 'object') {
        html += '<ul>';
        
        var valores = {
            'name': 'Nombre',
            'brand': 'Marca',
            'reference': 'Referencia',
            'cost_sale': 'Costo Venta',
            'warranty': 'Garantía',
            'remarks': 'Observaciones',
            'stock': 'Stock',
        }

        $.each(obj, function (key, value, valores) {
            html += '<li>' + valores[key] + ': ' + value + '</li>';
        });
        html += '</ul>';
        console.log(html);
        swal(
            {
                type: 'error',
                title: '¡Algo salió mal!',
                html: html,
            }
        );
    } else {
        html += '<p>' + obj + '</p>';
        console.log(html);
    }
}