# Generated by Django 4.2.2 on 2023-07-21 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_supplierpaymentbalance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplierpaymentbalance',
            old_name='amount',
            new_name='paid_amount',
        ),
    ]
