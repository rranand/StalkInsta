$(document).on('submit', '#user_form', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: 'img',
        data: $('#user_form').serialize(),
        dataType: 'html',
        success: function (data) {
            let x= $('.loadContent');
            x.innerHTML = '';
            x.html(data);
        }
    });
});