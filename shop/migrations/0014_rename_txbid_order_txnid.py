# Generated by Django 5.0.7 on 2024-08-09 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_order_txbid_order_txn_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='txbid',
            new_name='txnid',
        ),
    ]
