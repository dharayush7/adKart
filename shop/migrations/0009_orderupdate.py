# Generated by Django 5.0.7 on 2024-08-07 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_order_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=100)),
                ('order_desc', models.CharField(max_length=10000)),
                ('timpstamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
