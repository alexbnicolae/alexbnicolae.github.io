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
$(".js-add-friend").on("click", function(e){
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
$(document).ready(function(){
    setInterval(myTimer, 1000)
    // myTimer()
    
})


$(".clickFocus").on("click", function(e){
    var c = 0;
    var changeToFocus = document.querySelectorAll(".noFocus")
    changeToFocus.forEach(element => {
        if ( element.dataset.focus == "noFocus" )
            c++  
        element.dataset.focus = "focus"
        if ( element.dataset.focus == "focus" )  
        {
            $(".noRead").remove();
            $(".titleNoRead").empty();
        }    
    })
    var sender = $(".titleNoRead").data("sender")
    $(".titleNoRead").append("Chat - " + sender)
})

function myTimer(){
    $.ajax({
        type : "GET",
        url: $("#posts").data("url"),
        success: (response) => {
            var myDisPosts = document.querySelectorAll(".myPost")
            var friendDisPosts = document.querySelectorAll(".friendPost")

            var noRead = document.querySelectorAll(".noRead")
            var myDisPostsLen = 0
            var friendDisPostsLen = 0
            if(noRead.length >= 0)
                noRead = noRead.length

            if(myDisPosts.length >= 0 )
                 myDisPostsLen = myDisPosts.length
            

            if(  friendDisPosts.length >= 0)
                 friendDisPostsLen = friendDisPosts.length
                
            if(typeof(response.messages) == "object")
            {   
                if(myDisPostsLen+friendDisPostsLen < response.messages.length && myDisPostsLen+friendDisPostsLen>0)
                {       
                    var titleNoRead = response.messages.length - myDisPosts - friendDisPosts
                    
                    if(noRead < 1)
                    {
                        $(".titleNoRead").prepend("(" + titleNoRead + ")")
                        $("#posts").prepend("<div  class='noRead' >You have unread messages</div>")
                    }
                    
                }
                for(var i = myDisPostsLen+friendDisPostsLen; i < response.messages.length; i++)
                {   
                    console.log(response.messages[i])
                    var temp = ""
                    if (response.messages[i].sender_id == response.user)
                    {
                        temp = "<div id='messages' class='myPost flex flex-col space-y-4 p-3 scrollbar-thumb-blue scrollbar-thumb-rounded scrollbar-track-blue-lighter scrollbar-w-2 scrolling-touch'><div class='chat-message'><div class='flex items-end'><div class='flex flex-col  text-xs  mx-2 order-2 items-start'><div><span class=' px-4 py-2 rounded-lg inline-block rounded-bl-none bg-gray-300 text-gray-600'>" + response.messages[i].text
    
                        if (response.messages[i].file)
                        {
                            temp = temp + "<a href='/media/" + response.messages[i].file + "'><div>" + response.messages[i].file + "</div></a>"
                        }
    
                        temp = temp + "</span></div></div><img src='https://static.wikia.nocookie.net/caramella-girls/images/9/99/Blankpfp.png/revision/latest?cb=20190122015011' alt='My profile' class='w-6 h-6 rounded-full order-1'></div></div></div>"
                    }
                    else
                    {   
                        $(".titleNoRead").attr("data-sender", response.sender)
                        temp = temp + "<div id='messages' data-focus='noFocus' class=' friendPost noFocus flex flex-col space-y-4 p-3 scrollbar-thumb-blue scrollbar-thumb-rounded scrollbar-track-blue-lighter scrollbar-w-2 scrolling-touch justify-end'><div class='chat-message'><div class='flex justify-end'><div class='flex flex-col space-y-2 text-xs max-w-xs mx-2 order-1 justify-items-end'><div><span class='px-4 py-2 rounded-lg inline-block rounded-br-none bg-blue-600 text-white '>" + response.messages[i].text
    
                        if(response.messages[i].file)
                        {
                            temp = temp + "<a href='/media/" + response.messages[i].file +"'class='text-white' ><div>" + response.messages[i].file + "</div></a>"
                        }
    
                        temp  = temp + "</span></div></div><img src='https://static.wikia.nocookie.net/caramella-girls/images/9/99/Blankpfp.png/revision/latest?cb=20190122015011' alt='My profile' class='w-6 h-6 rounded-full order-2'></div></div></div>"

                        
                    }
                    $("#posts").prepend(temp)
                }
            }
        }

    });
}