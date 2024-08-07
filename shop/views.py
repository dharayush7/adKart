from django.http import HttpResponse 
from django.core import serializers 
import json
from django.shortcuts import render, redirect
from .models import Product, Contact, Order
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
        
        return render(request, "shop/orderSucess.html", {"id": order.order_id})
    return render(request, 'shop/checkout.html')

def search(request):
    return render(request, 'shop/orderSucess.html')