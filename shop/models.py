from django.db import models # type: ignore


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