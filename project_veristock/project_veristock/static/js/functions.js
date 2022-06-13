function message_error(obj) {
    var html = '';
    if(typeof (obj) == 'object') {
        html += '<ul>';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ': ' + value + '</li>';
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
    }
}