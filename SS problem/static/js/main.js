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
$(document).on("click", ".js-add-friend", function(e){
    e.preventDefault();
    const action = $(this).attr("data-action")
    $.ajax({
        type: "POST",
        url: $(this).data("url"),
        data: {
            action: action,
            username: $(this).data("username"),
        },
        success:(data) =>{
            $(this).text(data.wording)
            if(action=="Add Friend"){
                $(this).attr("data-action", "Unfriend")
            }
            else {
                $(this).attr("data-action", "Add Friend")
            }
        },

        error: (error) => {
            console.log(error)
        }
    });
})
.on("click", ".js-submit-me", function(e){
    e.preventDefault();
    console.log("Submit me?")
})