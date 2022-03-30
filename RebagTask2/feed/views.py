from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from feed.forms import GiftCardForm, OrderForm, UserGiftCardForm
from feed.models import GiftCard, Order, OrderHistory, UserGiftCard
from feed.serializers import GiftCardSerializer, OrderHistorySerializer, OrderSerializer, UserGiftCardSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.models import User
@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def card_list(request):
    if request.method == "GET":
        userGiftCards = UserGiftCard.objects.filter(user__id = request.user.id)
        serializer = UserGiftCardSerializer(userGiftCards, many=True)
        for x in serializer.data:
            for y in x:
                if y == "giftCard":
                    giftCard =  GiftCard.objects.get(id=x[y])
                    x[y] = GiftCardSerializer(giftCard).data
        return JsonResponse(serializer.data, status=200, safe=False)

    elif request.method == "POST":
        if request.user.is_staff is True:
            data = JSONParser().parse(request)
            serializer = GiftCardSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                messages.add_message(request, messages.SUCCESS, 'The gift card was successfully added.')
                return JsonResponse(serializer.data, status=200, safe=False)
            return JsonResponse(serializer.errors, status=400, safe=False)
                
@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def order_list(request):

    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            orderSaved = Order.objects.get(orderNumber=data['orderNumber'])

            gc = UserGiftCard.objects.get(id=orderSaved.giftCard.id)
            amount = Decimal(gc.amount) - Decimal(data['amount'])
            amount = Decimal(amount)
            if amount < 0:
                return JsonResponse({
                    "error":"You don't have enough money to do this order!"
                }, status=400)
                
            dataGc = {
                "user": gc.user.id,
                "giftCard": gc.giftCard.id,
                "amount": amount,
            }
            specializer3 = UserGiftCardSerializer(gc, data = dataGc)
            
            if specializer3.is_valid():
                specializer3.save()

            pushArray = [orderSaved.id, data['productOrdered'],  data['amount'], data['date'], data['orderNumber'] ]

            orderH = OrderHistory.objects.get(giftCard__id=data["giftCard"])
            array = orderH.logHistory 
            array.append(pushArray)

            dataOrderHistory = {
            'giftCard' : data['giftCard'],
            'logHistory': array
            }

            serializer2 = OrderHistorySerializer(orderH, data=dataOrderHistory)
            
            if serializer2.is_valid():
                serializer2.save()
            messages.add_message(request, messages.SUCCESS, 'Your order was successfully added.')
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_order_history(request, pk):
    try:
        orderH = OrderHistory.objects.get(id=pk)
    except Exception as e:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = OrderHistorySerializer(orderH)
        return JsonResponse(serializer.data)

@csrf_exempt
@api_view(['PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def order_detail(request, pk):
    try:
        getOrder = Order.objects.get(id=pk)
        gc = UserGiftCard.objects.get(id=getOrder.giftCard.id)
        gca = GiftCard.objects.get(id=gc.giftCard.id)
    except Exception as e:
        return HttpResponse(status = 404)

    if gca.available == True:
        if request.method == "PUT":
            data = JSONParser().parse(request)

            amount = Decimal(gc.amount) + Decimal(getOrder.amount) - Decimal(data['amount'])
            amount = Decimal(amount)
            if amount < 0:
                return JsonResponse({
                    "error":"You don't have enough money to do this order!"
                }, status=400)
            dataGc = {
                "user": gc.user.id,
                "giftCard": gc.giftCard.id,
                "amount": amount,
            }
            specializer3 = UserGiftCardSerializer(gc, data = dataGc)
            if specializer3.is_valid():
                specializer3.save()

            pushArray = [getOrder.id, data["productOrdered"],  data['amount'], data['date'], data['orderNumber'], ]

            orderH = OrderHistory.objects.get(giftCard__id=data["giftCard"])
            array = orderH.logHistory 

            for x in array:
                if getOrder.orderNumber in x:
                    array.remove(x)

            array.append(pushArray)
            dataOrderHistory = {
                'giftCard' : data['giftCard'],
                'logHistory': array,
            }

            serializer = OrderSerializer(getOrder, data=data)
            serializer2 = OrderHistorySerializer(orderH, data = dataOrderHistory)

            if serializer2.is_valid():
                serializer2.save()

            if serializer.is_valid():
                serializer.save()
                messages.add_message(request, messages.INFO, 'Your order was successfully edited.')
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        
        elif request.method == "DELETE":
            orderH = OrderHistory.objects.get(giftCard__id=getOrder.giftCard.id)
            array = orderH.logHistory 
            for x in array:
                if getOrder.orderNumber in x:
                    array.remove(x)
            dataOrderHistory = {
                'giftCard' : getOrder.giftCard.id,
                'logHistory': array,
            }        
            serializer2 = OrderHistorySerializer(orderH, data = dataOrderHistory)

            if serializer2.is_valid():
                serializer2.save()

            amount = Decimal(gc.amount) + Decimal(getOrder.amount)
            amount = Decimal(amount)
            
            dataGc = {
                "user": gc.user.id,
                "giftCard": gc.giftCard.id,
                "amount": amount,
            }
            specializer3 = UserGiftCardSerializer(gc, data = dataGc)
        
            if specializer3.is_valid():
                specializer3.save()
            getOrder.delete()
            messages.add_message(request, messages.WARNING, 'Your order was successfully deleted.')
            return HttpResponse(status=204)
    
# def generateToken(request):
#     template = "generateToken.html"
    
#     try:
#         token = Token.objects.get(user=request.user)
#     except Exception as e:
#         ...
    
#     context = {
#         "token":token,
#     }
#     return render(request, template, context)

def home(request):
    template = "home.html"
    context = {

    }
    return render(request, template, context)

def displayCards(request):
    template = "gift_card_show.html"
    token = Token.objects.get(user=request.user)
    
    context = {
        "token":token,
    }
    return render(request, template, context)

def add_gift_card(request):
    template = "add_gift_card.html"
    form = GiftCardForm()
    token = Token.objects.get(user=request.user)
    context = {
        "form": form,
        "token":token,
    }
    return render(request, template, context)

def add_order_form(request, pk):
    template = "add_order_form.html"
    giftCard = UserGiftCard.objects.get(id=pk)
    orderHistory = OrderHistory.objects.get(giftCard__id=giftCard.id)
    token = Token.objects.get(user=request.user)
    form = OrderForm()
    context = {
        'form': form,
        'giftCard': giftCard,
        'token':token,
        'orderHistory':orderHistory,
    }
    return render(request, template, context)

def edit_order_form(request, pk):

    template = "edit_order_form.html"
    order = Order.objects.get(id=pk)
    gc = GiftCard.objects.get(id=order.giftCard.giftCard.id)
    token = Token.objects.get(user=request.user)

    context = {
        "order": order,
        "token": token,
        "gc": gc,
    }
    return render(request, template, context)

def get_order_history_template(request, pk):
    template = "get_order_history_template.html"
    orderH = OrderHistory.objects.get(giftCard__id=pk)
    token = Token.objects.get(user=request.user)
    gc = GiftCard.objects.get(id=orderH.giftCard.giftCard.id)
    context = {
        "token": token,
        "orderH":orderH,
        "gc":gc
    }
    return render(request, template, context)


# ADMIN ZONE

@csrf_exempt
@api_view(['GET','POST','PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def admin_gift_card(request):
    if request.user.is_staff is True:
        if request.method == "GET":
            collectGC = GiftCard.objects.all()
            serializerCGC = GiftCardSerializer(collectGC, many=True)
            return JsonResponse(serializerCGC.data, status=200, safe=False)

        elif request.method == "POST":
            data = JSONParser().parse(request)
            responseData = []
            for user in data["users"]:
                data = {
                    "user": user,
                    "giftCard": data["giftCard"],
                    "amount": Decimal(data["amount"]),
                }
                serializer = UserGiftCardSerializer(data=data)
                username = User.objects.get(id=data["user"])
                giftCardName = GiftCard.objects.get(id=data["giftCard"])
                if serializer.is_valid():
                    serializer.save()
                    responseData.append(serializer.data)
                    messages.add_message(request, messages.SUCCESS, f'The {giftCardName.name} was successfully added to {username}.')
                else:
                    messages.add_message(request, messages.WARNING, f'The {giftCardName.name} was not added to {username}.')
                    responseData.append(serializer.errors)
            
            return JsonResponse(responseData, safe=False) 

        elif request.method == "PUT":
            data = JSONParser().parse(request)
            responseData = []
            for user in data["users"]:
                getUserGC = UserGiftCard.objects.filter(user__id=user, giftCard__id=data["giftCard"]).first()
                username = User.objects.get(id=user)
                giftCardName = GiftCard.objects.get(id=data["giftCard"])
                if getUserGC != None:
                    data = {
                        "user": user,
                        "giftCard": data["giftCard"],
                        "amount": Decimal(data["amount"]),
                    }
                    serializer = UserGiftCardSerializer(getUserGC, data=data)
                    if serializer.is_valid():
                        serializer.save()
                        responseData.append(serializer.data)
                        messages.add_message(request, messages.INFO, f'The {giftCardName.name} was successfully edited to {username}.')
                    else:
                        responseData.append(serializer.errors)
                else:
                    messages.add_message(request, messages.WARNING, f'The {giftCardName.name} was not edited to {username}.')
            return JsonResponse(responseData, safe=False) 

        elif request.method == "DELETE":
            data = JSONParser().parse(request)
            for user in data["users"]:
                getUserGC = UserGiftCard.objects.filter(user__id=user, giftCard__id=data["giftCard"]).first()
                username = User.objects.get(id=user)
                giftCardName = GiftCard.objects.get(id=data["giftCard"])
                getUserGC.delete()
                messages.add_message(request, messages.WARNING, f'Your {giftCardName.name} was successfully deleted for {username}.')
            return HttpResponse(status=204)

@csrf_exempt
@api_view(['PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def admin_manipulate_a_gc(request, pk):
    if request.user.is_staff is True:
        if request.method == "PUT":
            data = JSONParser().parse(request)
            print(data)
            getGC = GiftCard.objects.get(id=pk)
            serializer = GiftCardSerializer(getGC, data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        elif request.method == "DELETE":
            getGC = GiftCard.objects.get(id=pk)
            getGC.delete()
            messages.add_message(request, messages.WARNING, f'The {getGC.name} was successfully deleted.')
            return HttpResponse(status=204)


def admin_gift_card_user_post(request):
    template = "admin_zone/admin_gift_card_user_post.html"
    token = Token.objects.get(user=request.user)
    form = UserGiftCardForm()
    context = {
        "form":form,
        "token":token,
    }
    return render(request, template, context)


def admin_gift_card_user_edit(request):
    template = "admin_zone/admin_gift_card_user_edit.html"
    token = Token.objects.get(user=request.user)
    form = UserGiftCardForm()
    context = {
        "form":form,
        "token":token,
    }
    return render(request, template, context)

def admin_gift_card_user_delete(request):
    template = "admin_zone/admin_gift_card_user_delete.html"
    token = Token.objects.get(user=request.user)
    form = UserGiftCardForm()
    context = {
        "form":form,
        "token":token,
    }
    return render(request, template, context)

def admin_zone_page(request):
    template = "admin_zone/admin_zone.html"
    context = {

    }
    return render(request, template, context)

def admin_display_gc(request):
    template = "admin_zone/admin_display_gc.html"
    collectGC = GiftCard.objects.all()
    token = Token.objects.get(user=request.user)
    context = {
        "collectGC":collectGC,
        "token":token,
    }
    return render(request, template, context)
