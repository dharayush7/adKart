# Generated by Django 5.0.7 on 2024-08-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='order_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
