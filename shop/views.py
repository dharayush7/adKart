from django.http import HttpResponse 
from django.core import serializers 
import json
from django.shortcuts import render, redirect
from .models import Product, Contact, Order, OrderUpdate
from math import ceil


# Create your views here.

def index(request):
    def nSlide(length: int):
        return (length // 3) + ceil((length / 3) - (length // 3))

    allProds = []

    catList = Product.objects.values('category')
    cats = {item['category'] for item in catList}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        allProds.append([prod, range(1, nSlide(len(prod)))])

    params = {
        'allProds': allProds
    }
    return render(request, 'shop/index.html', params)


def about(request):        
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        frsName = request.POST.get('frsName', '')
        lstName = request.POST.get('lstName', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        name = frsName +" "+ lstName
        contact = Contact(name=name, email=email, phone=phone, desc=desc )
        contact.save()
        return redirect('contactSuccess')
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get("orderId")
        email = request.POST.get("email")
        try:
            order = Order.objects.filter(order_id=orderId)
            if len(order)>0:
                if order[0].email == email:
                    addr = {
                        "name": order[0].name,
                        "adrln1": order[0].address_line_1,
                        "adrln2": order[0].address_line_2,
                        "csp": order[0].district+ ", "+ order[0].state + " - " + order[0].pincode,
                        "ph": order[0].phone,
                        "email": order[0].email
                    }

                    tp = 0 
                    prod = []
                    items = json.loads((order[0].items_json))
                    keys = list(items.keys())
                    for key in keys:
                        id = key[2:]
                        prd = Product.objects.filter(id=id)
                        sbTl = prd[0].price * items[key]
                        tp = tp + sbTl
                        prdApp = [prd[0].product_name, items[key], sbTl]
                        prod.append(prdApp)
                    
                    status = OrderUpdate.objects.filter(order_id=orderId)
                    print(status[0].timpstamp)
                    params = {
                        "addr": addr,
                        "total": tp,
                        "product": prod,
                        "status": status
                    }

                    return render(request, 'shop/trackDetails.html', params)
                    
                else:
                    return render(request, "shop/trackFailed.html")
            else:
                return render(request, "shop/trackFailed.html")

        except:
            return render(request, "shop/trackFailed.html")
    return render(request, 'shop/tracker.html')


def product(request, id):
    prd = Product.objects.filter(id=id)
    return render(request, 'shop/product.html', {'prd': prd})


def contactSuccess(request):
    return render(request, 'shop/contactSuccess.html')


def cart(request):
    if request.method == "POST":
        body = json.loads(request.body)
        id = body[2:]
        ob = Product.objects.filter(id=id)
        ob_js = serializers.serialize("json", ob)
        return HttpResponse(ob_js)

    return render(request, "shop/cart.html")


def checkout(request):
    if request.method == "POST":
        itemJson = request.POST.get("itemJson", '')
        fullname = request.POST.get("fullname", '')
        email = request.POST.get("email", '')
        adel1 = request.POST.get("adel1", '')
        adrl2 = request.POST.get("adrl2", '')
        district = request.POST.get("district", '')
        state = request.POST.get("state", '')
        pincode = request.POST.get("pincode", '')
        ph = request.POST.get("ph", '')
        order = Order(items_json=itemJson, name=fullname, email=email, address_line_1=adel1, address_line_2=adrl2, district=district, state=state, pincode=pincode, phone=ph)
        order.save()
        update = OrderUpdate(order_id= order.order_id, order_desc="Order has been placed")
        update.save()
        return render(request, "shop/orderSucess.html", {"id": order.order_id})
    return render(request, 'shop/checkout.html')


def search(request):
    return render(request, 'shop/trackDetails.html')