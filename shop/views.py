from django.shortcuts import render, redirect # type: ignore
from .models import Product, Contact
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