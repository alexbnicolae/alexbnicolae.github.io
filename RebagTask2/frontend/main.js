$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;


            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i += 1) {
                    const cookie = jQuery.trim(cookies[i]);

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

$(".displayCards").ready(function(){ 
    var token = $('.displayCards').data('token')
    
    $.ajax({
        type: "GET",
        headers: {'Authorization':`Token ${token}`},
        url: $('.displayCards').data("url"),
        success: (response) => {
            if (typeof(response) == 'object'){
            response.forEach(element => {
                console.log(element)
                var available
                var cardDesign
                if (element.giftCard.available == true)
                    available = `Yes`
                else
                    available = `No`

                cardDesign = `<div class="inline-block border-black border-2 border-solid rounded-lg p-4 bg-yellow-200">
                    <div class="border-black border-b-2 border-solid  p-2 ">
                        <div class="flex justify-center text-xl font-bold">&bull;Card Name:</div>
                        <div class="flex justify-center text-xl font-bold text-blue-500">${element.giftCard.name}</div>
                    </div>
                    <div class="p-2">
                        <div class="flex justify-center text-xl font-bold">&bull;Amount:</div>
                        <div class="flex justify-center text-xl font-bold text-blue-500">${element.amount}</div>
                    </div>
                    <div class="border-black border-t-2 border-solid p-2 ">
                        <div class="flex justify-center text-xl font-bold">&bull;Available:</div>
                        <div class="flex justify-center text-xl font-bold text-blue-500">${available}</div>
                    </div>`
                if(available == 'Yes')
                    cardDesign = `${cardDesign}<div class="flex justify-evenly p-2">
                        <a href='/add_order/${element.id}' class="border-2 border-solid border-gray-400 rounded-lg p-1 text-black bg-yellow-400 font-bold">Order</a>
                        <a href="/allOrders/${element.id}" class="border-2 border-solid border-gray-400 rounded-lg p-1 bg-green-400 font-bold">Order History</a>
                    </div></div>`
                else 
                    cardDesign = `${cardDesign}<div class="flex justify-evenly p-2">
                    <a href="/allOrders/${element.id}" class="border-2 border-solid border-gray-400 rounded-lg p-1 bg-green-400 font-bold">Order History</a>
                    </div></div>`

                $('#displayCards').append(cardDesign)
            });
            }
        }
    })
})

$(".orderHistory").ready(function(){
    const token = $('.orderHistory').data('token')
    const url = $(this).attr("data-url")
    $.ajax({
        type: "GET",
        headers: {'Authorization':`Token ${token}`},
        url: $('.orderHistory').data("url"),
        success: (response) => {
            const avaialble = $('#orderHistory').attr("data-true")
            if (typeof(response) == 'object'){
                response.logHistory.forEach(element => {
                    cardDesign = `<div id="orderHistory" class="inline-block border-black border-2 border-solid rounded-lg p-4 bg-yellow-200">
                        <div class="border-black border-b-2 border-solid  p-2 ">
                            <div class="flex justify-center text-xl font-bold">&bull;Order Number:</div>
                            <div class="flex justify-center text-xl font-bold text-blue-500">${element[4]}</div>
                        </div>
                        <div class="border-black border-b-2 border-solid  p-2 ">
                            <div class="flex justify-center text-xl font-bold">&bull;Product Ordered:</div>
                            <div class="flex justify-center text-xl font-bold text-blue-500">${element[1]}</div>
                        </div>
                        <div class="p-2">
                            <div class="flex justify-center text-xl font-bold">&bull;Amount:</div>
                            <div class="flex justify-center text-xl font-bold text-blue-500">${element[2]}</div>
                        </div>
                        <div class="border-black border-t-2 border-solid p-2 ">
                            <div class="flex justify-center text-xl font-bold">&bull;Date:</div>
                            <div class="flex justify-center text-xl font-bold text-blue-500">${element[3]}</div>
                        </div>
                    `
                    
                    if(avaialble == "True")
                    {
                        
                        cardDesignLinks=`${cardDesign}<div id="links" class="flex justify-evenly p-2">
                        <a href='/edit_order/${element[0]}' class="border-2 border-solid border-gray-400 rounded-lg p-1 text-black bg-yellow-400  font-bold">Edit</a>
                        <button class="border-2 border-solid border-gray-400 rounded-lg p-1 bg-red-400 font-bold js-delete-order" data-delete="/order_detail/${element[0]}" data-token-order=${token}>Delete</button>
                            </div>
                        </div>`
                        $('#orderHistory').append(cardDesignLinks)

                        $(".js-delete-order").on("click",function(e) {
                            var token = $(this).attr('data-token-order')
                            var url = $(this).attr('data-delete')
                            console.log(url)
                            $.ajax({
                                type: "DELETE",
                                url:url,
                                headers: {'Authorization':`Token ${token}`},
                                contentType: "application/json",
                                success:() => {
                                    location.replace("/displayCards")
                                }
                            })
                        })
                    }
                    else 
                        $('#orderHistory').append(cardDesign)
                })

            }
        }  
    })
})

$(".js-submit").on("click", function(e){
    e.preventDefault()
    var token = $('.order').data('token')

    var randomNumber = Math.floor((Math.random() * 10000) + 1);

    var today = new Date();
    var dateM = `${today.getFullYear()}-${today.getMonth()+1}-${today.getDate()}`;
    var time = `${today.getHours()}:${today.getMinutes()}:${today.getSeconds()}`;
    var dateTime = `${dateM} ${time}`;

    const giftCard = $(".gc-add").val()
    const productOrder = $(".po-add").val()
    const amount = $(".a-add").val()
    const clickDate = dateTime
    const orderNumber = randomNumber

    const data = {
        giftCard : giftCard,
        productOrdered : productOrder,
        amount: amount,
        date: clickDate,
        orderNumber: orderNumber,
    }
    const url = $(this).data("url")
    

    $.ajax({
        type:"POST",
        url: url,
        headers: {'Authorization':`Token ${token}`},
        data:JSON.stringify(data),
        contentType: "application/json",
        success: () => {
            location.replace("/displayCards")
        },
        error: (e) => {
            const error = e.responseJSON.error
            $(".errors-add-order").append("<div>&bull;" + error.toUpperCase() + "</div>")

        }

    })

})

$(".js-edit").on("click", function(e) {
    e.preventDefault()

    var token = $('.order').data('token')
    const url = $(this).data("url")


    var today = new Date();
    var dateM = `${today.getFullYear()}-${today.getMonth()+1}-${today.getDate()}`;
    var time = `${today.getHours()}:${today.getMinutes()}:${today.getSeconds()}`;
    var dateTime = `${dateM} ${time}`;
    
    const giftCard = $(".gc-put").val()
    const productOrder = $(".po-put").val()
    const amount = $(".a-put").val()
    const clickDate = dateTime
    const orderNumber = $(".on-put").val()

    const data = {
        giftCard : giftCard,
        productOrdered : productOrder,
        amount: amount,
        date: clickDate,
        orderNumber: orderNumber,
    }

    $.ajax({
        type:"PUT",
        url:url,
        headers: {'Authorization':`Token ${token}`},
        data:JSON.stringify(data),
        contentType: "application/json",
        success: () => {
            location.replace("/displayCards")
        },
        error: (error) => {
            for(const x in error.responseJSON){
                error.responseJSON[x].forEach(element => {
                    $(".errors-edit-order").append("<div>&bull;" + element.toUpperCase() + "</div>")
                });
            }
        }
    })
})

$(".js-add-giftCard").on("click", function(e){
    e.preventDefault()
    const url = $(this).attr("data-url")
    const token = $(this).attr("data-token")
    
    console.log(token, url)

    const name = $(".name-add").val()
    const available = $(".available-add").val()

    const data = {
        name: name,
        available: available,
    }
    $.ajax({
        type:"POST",
        url:url,
        headers: {'Authorization':`Token ${token}`},
        data:JSON.stringify(data),
        contentType: "application/json",
        success: () => {
            location.replace("/displayCards")
        },
        error: (error) => {
            for(const x in error.responseJSON){
                error.responseJSON[x].forEach(element => {
                    $(".errors-add-giftCard").append("<div>&bull;" + element.toUpperCase() + "</div>")
                });
            }
        }

    })
})

$(".js-admin-add-giftCard").on("click", function(e){
    e.preventDefault()
    const url = $(this).attr("data-url")
    const token = $(this).attr("data-token")

    const adminUserAdd = $(".admin-user-add").val() 
    const adminGiftCardAdd = $(".admin-giftCard-add").val()
    const adminAmountAdd = $(".admin-amount-add").val()

    const data = {
        users : adminUserAdd,
        giftCard : adminGiftCardAdd,
        amount: adminAmountAdd,
    }

    $.ajax({
        type: "POST",
        url: url,
        headers: {'Authorization':`Token ${token}`},
        data:JSON.stringify(data),
        contentType: "application/json",
        success: () => {
            location.replace("/displayCards")
        },
        error: (error) => {
            for(const x in error.responseJSON){
                error.responseJSON[x].forEach(element => {
                    $(".errors-add-admin-giftCard").append("<div>&bull;" + element.toUpperCase() + "</div>")
                });
            }
        }
    })
})


$(".js-admin-edit-giftCard").on("click", function(e){
    e.preventDefault()
    const url = $(this).attr("data-url")
    const token = $(this).attr("data-token")

    const adminUserEdit = $(".admin-user-edit").val() 
    const adminGiftCardEdit = $(".admin-giftCard-edit").val()
    const adminAmountEdit = $(".admin-amount-edit").val()

    const data = {
        users : adminUserEdit,
        giftCard : adminGiftCardEdit,
        amount: adminAmountEdit,
    }

    $.ajax({
        type: "PUT",
        url: url,
        headers: {'Authorization':`Token ${token}`},
        data:JSON.stringify(data),
        contentType: "application/json",
        success: () => {
            location.replace("/displayCards")
        },
        error: (error) => {
            for(const x in error.responseJSON){
                error.responseJSON[x].forEach(element => {
                    $(".errors-edit-admin-giftCard").append("<div>&bull;" + element.toUpperCase() + "</div>")
                });
            }
        }
    })
})

$(".js-admin-delete-giftCard").on("click", function(e){
    e.preventDefault()
    const url = $(this).attr("data-url")
    const token = $(this).attr("data-token")

    const adminUserDelete = $(".admin-user-delete").val() 
    const adminGiftCardDelete = $(".admin-giftCard-delete").val()
    const adminAmountDelete = $(".admin-amount-delete").val()

    const data = {
        users : adminUserDelete,
        giftCard : adminGiftCardDelete,
        amount: adminAmountDelete,
    }

    $.ajax({
        type: "DELETE",
        url: url,
        headers: {'Authorization':`Token ${token}`},
        data:JSON.stringify(data),
        contentType: "application/json",
        success: () => {
            location.replace("/displayCards")
        },
        error: (error) => {
            for(const x in error.responseJSON){
                error.responseJSON[x].forEach(element => {
                    $(".errors-delete-admin-giftCard").append("<div>&bull;" + element.toUpperCase() + "</div>")
                });
            }
        }
    })
})
