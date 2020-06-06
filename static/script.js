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


function hideLoader() {
    try {
      let x = document.getElementById("resultant").complete;

      if (x===true) {
        document.getElementById("loader").style.display = 'none';
      }
    } catch (e) {}
}

setInterval(hideLoader, 100);

function hideIt() {
    $('.loadContent').empty();
}