# Generated by Django 4.2.2 on 2023-07-11 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=255)),
                ('supplier_email_address', models.CharField(max_length=255)),
                ('supplier_phone_number', models.CharField(max_length=255)),
                ('supplier_kra_pin', models.CharField(max_length=255)),
                ('supplier_bank_1', models.CharField(max_length=255)),
                ('supplier_bank_1_number', models.CharField(max_length=255)),
                ('supplier_bank_2', models.CharField(max_length=255)),
                ('supplier_bank_2_number', models.CharField(max_length=255)),
            ],
        ),
    ]