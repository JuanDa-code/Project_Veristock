function message_error(obj) {
    console.log(obj);
    var html = '';
    if(typeof (obj) == 'object') {
        html += '<ul>';
        

        $.each(obj, function (key, value) {
            var valores = {
                'name': 'Nombre',
                'brand': 'Marca',
                'reference': 'Referencia',
                'cost_sale': 'Costo Venta',
                'warranty': 'Garantía',
                'remarks': 'Observaciones',
                'stock': 'Stock',
                'date' : 'Fecha',
                'reason': 'Motivo',
                'id_product' : 'Producto'
            }
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