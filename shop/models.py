from django.db import models 


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100, default="UNNAMED")
    desc = models.CharField(max_length=300, default="")
    category = models.CharField(max_length=50, default="Uncategorized")
    sub_category = models.CharField(max_length=50, default="Uncategorized")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default="shop/images/default.png")
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    desc = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=1000)
    address_line_2 = models.CharField(max_length=1000)
    district = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    pincode = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default="")
    txn_status = models.CharField(max_length=50, default="pending")
    txnid = models.CharField(max_length=50, default="")


    

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=100)
    order_desc = models.CharField(max_length=10000)
    timpstamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_desc[0:7] + "..."


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=100, default="")
    mihpayid= models.CharField(max_length=100)
    mode= models.CharField(max_length=100)
    status= models.CharField(max_length=100)
    txnid= models.CharField(max_length=100)
    amount= models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    hash=models.CharField(max_length=10000)
    payment_source=models.CharField(max_length=100)
    bank_ref_num=models.CharField(max_length=100)
    bankcode=models.CharField(max_length=100)
    error_Message=models.CharField(max_length=100)
    error=models.CharField(max_length=100)
    addedon=models.CharField(max_length=100)
