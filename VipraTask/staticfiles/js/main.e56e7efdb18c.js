$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;


            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i += 1) {
                    const cookie = jQuery.trim(cookies[i]);

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }

            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    },
});
$(document).on("click", ".js-submit", function(e){
    e.preventDefault();
    const first_name = $(".fn-add").val()
    const last_name = $(".ln-add").val()
    const email = $(".email-add").val()
    const phoneNumber = $(".pn-add").val()
    const data = {
        first_name: first_name,
        last_name: last_name,
        email: email,
        phoneNumber: phoneNumber,
    }
    $.ajax({
        type: "POST",
        url:$(this).data("url"),
        data: JSON.stringify(data),
        contentType: "application/json",
        success:() => {
            location.replace("/")
        },
        error: (error) => {
            for(const x in error.responseJSON){
                error.responseJSON[x].forEach(element => {
                    $(".errors").append("<div>&bull;" + element.toUpperCase() + "</div>")
                });
            }
        }
    })
})
.on("click", ".js-edit", function(e){
    e.preventDefault();
    const first_name = $(".fn-edit").val()
    const last_name = $(".ln-edit").val()
    const email = $(".email-edit").val()
    const phoneNumber = $(".pn-edit").val()
    const data = {
        first_name: first_name,
        last_name: last_name,
        email: email,
        phoneNumber: phoneNumber,
    }
    $.ajax({
        type: "PUT",
        url:$(this).data("url"),
        data: JSON.stringify(data),
        contentType: "application/json",
        success:() => {
            location.replace("/")
        },
        error: (error) => {
            for(const x in error.responseJSON){
                error.responseJSON[x].forEach(element => {
                    $(".errors-edit").append("<div>&bull;" + element.toUpperCase() + "</div>")
                });
            }
        }
    })
})
.on("click", ".js-delete", function(e){
    e.preventDefault();
    $.ajax({
        type: "DELETE",
        url:$(this).data("url"),
        contentType: "application/json",
        success:() => {
            location.replace("/")
        }
    })
})