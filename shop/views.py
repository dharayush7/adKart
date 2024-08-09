from django.http import HttpResponse 
from django.core import serializers 
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, redirect
from .models import Product, Contact, Order, OrderUpdate, Transaction
from .payments.payUHasher import generate_hash
from .payments.payUCreads import merchant_key
from .payments.txn import createTxnId
from .payments.payUBodyParser import payUParse
from math import ceil

from shop.payments import payUCreads



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

                    prod = []
                    items = json.loads((order[0].items_json))
                    keys = list(items.keys())
                    for key in keys:
                        id = key[2:]
                        prd = Product.objects.filter(id=id)
                        sbTl = prd[0].price * items[key]
                        prdApp = [prd[0].product_name, items[key], sbTl]
                        prod.append(prdApp)
                    
                    status = OrderUpdate.objects.filter(order_id=orderId)
                    print(status[0].timpstamp)
                    params = {
                        "addr": addr,
                        "total": order[0].amount,
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
        amount = request.POST.get("amount", 0)
        order = Order(items_json=itemJson, amount=amount,name=fullname, email=email, address_line_1=adel1, address_line_2=adrl2, district=district, state=state, pincode=pincode, phone=ph, txn_status="pending", txnid="")
        order.save()
        update = OrderUpdate(order_id= order.order_id, order_desc="Payment Initiated")
        update.save()
        
        txnid = createTxnId()
        payparam = {
            "txnid": txnid,
            "amount": order.amount,
            "productinfo": order.order_id,
            "firstname": order.name,
            "email": order.email,
        }
        hash = generate_hash(payparam)
        transaction = Transaction(order_id=order.order_id, mihpayid="",mode="", status="pending", txnid=txnid, amount=order.amount, firstname=order.name, email=order.email, hash=hash,payment_source="",bank_ref_num="",bankcode="", error_Message="", error="", addedon="" )
        transaction.save()
        key = merchant_key().get("key")
        params ={
            "key": key,
            "txnid": txnid,
            "productinfo": order.order_id,
            "amount": order.amount,
            "email": order.email,
            "firstname": order.name,
            "surl": "https://api.ayushananda.com/shop/ordersucess/",
            "furl": "https://api.ayushananda.com/shop/orderfailed/",
            "phone": order.phone,
            "hash": hash
        }

        return render(request, "shop/payu.html", params)
    return render(request, 'shop/checkout.html')


def search(request):
    return render(request, 'shop/trackDetails.html')

@csrf_exempt
def ordersucess(request):
    if request.method == "POST":
        body = payUParse(request.body)
        productinfo = body["productinfo"]
        transaction = Transaction.objects.filter(txnid=body["txnid"])
        if merchant_key()["key"] == body["key"]:
            order = Order.objects.filter(order_id=productinfo)
            
            order.update(txn_status="success",txnid=body["txnid"] )
            
            
            mihpayid = body['mihpayid']
            mode = body["mode"]
            payment_source = body["payment_source"]
            bank_ref_num = body["bank_ref_num"]
            bankcode = body["bankcode"]
            error = body["error"]
            error_Message = body["error_Message"]
            addedon = body["addedon"]
            status = body["status"]

            transaction.update(mihpayid=mihpayid, mode=mode, payment_source=payment_source, bank_ref_num=bank_ref_num, bankcode=bankcode, error=error, error_Message=error_Message, addedon=addedon, status=status)
            update1 = OrderUpdate(order_id=productinfo, order_desc="Payment success")
            update1.save()
            update2 = OrderUpdate(order_id=productinfo, order_desc="Order placed")
            update2.save()


            return render(request, "shop/orderSucess.html", {
                "id": order[0].order_id,
                "txnId": transaction[0].txnid
            })
        else:
            order = Order.objects.filter(order_id=productinfo)
            order.update(txn_status="failed due MID unmatch",txnid=body["txnid"] )
            
            
            update1 = OrderUpdate(order_id=productinfo, order_desc="Payment faild")
            update1.save()
            update2 = OrderUpdate(order_id=productinfo, order_desc="Order canceled due payment failed")
            update2.save()

            # failed due hash unmatch
            mihpayid = body['mihpayid']
            mode = body["mode"]
            payment_source = body["payment_source"]
            bank_ref_num = body["bank_ref_num"]
            bankcode = body["bankcode"]
            error = body["error"]
            error_Message = body["error_Message"]
            addedon = body["addedon"]
            status = "Failed due MID unmatch"

            transaction.update(mihpayid=mihpayid, mode=mode, payment_source=payment_source, bank_ref_num=bank_ref_num, bankcode=bankcode, error=error, error_Message=error_Message, addedon=addedon, status=status)


            return render(request, "shop.orderFailed.html", {
                "id": order[0].order_id,
                "txnId": transaction[0].txnid
            })
    else:
        return HttpResponse("404 bad request..")


@csrf_exempt
def orderFailed(request):
    if request.method == "POST":
        body = payUParse(request.body)
        print(body)
        productinfo = body["productinfo"]
        transaction = Transaction.objects.filter(txnid=body["txnid"])
        order = Order.objects.filter(order_id=productinfo)
        order.update(txn_status="failed due MID unmatch",txnid=body["txnid"] )
            
            
        update1 = OrderUpdate(order_id=productinfo, order_desc="Payment failed")
        update1.save()
        update2 = OrderUpdate(order_id=productinfo, order_desc="Order canceled due payment failed")
        update2.save()

           
        mihpayid = body['mihpayid']
        mode = "failed"
        payment_source = body["payment_source"]
        bank_ref_num = "NA"
        bankcode = "NA"
        error = body["error"]
        error_Message = body["error_Message"]
        addedon = body["addedon"]
        status = body["status"]

        transaction.update(mihpayid=mihpayid, mode=mode, payment_source=payment_source, bank_ref_num=bank_ref_num, bankcode=bankcode, error=error, error_Message=error_Message, addedon=addedon, status=status)
        return render(request, "shop/orderFailed.html", {
                "id": order[0].order_id,
                "txnId": transaction[0].txnid
            })

        
    else:
        return HttpResponse("404 bad request..")

# return render(request, "shop.orderFailed.html", {
#                 "id": order[0].order_id,
#                 "txnId": transaction[0].txnid
#             })