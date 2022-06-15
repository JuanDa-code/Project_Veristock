function message_error(obj) {
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
                'id_product' : 'Producto',
                'first_name': 'Primer nombre',
                'second_name': 'Segundo nombre',
                'last_names': 'Apellidos',
                'type_document': 'Tipo de documento',
                'document_number': 'Número de documento',
                'id_position': 'Cargo',
                'password': 'Contraseña',
                'state': 'Estado',
                'date_birth': 'Fecha cumpleaños',
                'phone': 'Teléfono',
                'email_address': 'Correo electrónico'
            }
            html += '<li>' + valores[key] + ': ' + value + '</li>';
        });
        html += '</ul>';
        swal(
            {
                type: 'error',
                title: '¡Algo salió mal!',
                html: html,
            }
        );
    } else {
        html += '<p>' + obj + '</p>';
        swal(
            {
                type: 'error',
                title: '¡Algo salió mal!',
                html: html,
            }
        );
    }
}