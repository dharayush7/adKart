# Generated by Django 5.0.7 on 2024-08-07 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address_line_1', models.CharField(max_length=1000)),
                ('address_line_2', models.CharField(max_length=1000)),
                ('district', models.CharField(max_length=1000)),
                ('state', models.CharField(max_length=1000)),
                ('pincode', models.CharField(max_length=100)),
            ],
        ),
    ]
