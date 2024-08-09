# Generated by Django 5.0.7 on 2024-08-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_order_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mihpayid', models.CharField(max_length=100)),
                ('mode', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('txnid', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('hash', models.CharField(max_length=10000)),
                ('payment_source', models.CharField(max_length=100)),
                ('bank_ref_num', models.CharField(max_length=100)),
                ('bankcode', models.CharField(max_length=100)),
                ('error_Message', models.CharField(max_length=100)),
                ('error', models.CharField(max_length=100)),
                ('addedon', models.CharField(max_length=100)),
            ],
        ),
    ]
