# Generated by Django 4.2.2 on 2023-07-11 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=25)),
                ('make', models.CharField(max_length=25)),
                ('type', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=25)),
                ('carrying_weight', models.IntegerField()),
                ('carrying_weight_metric', models.CharField(max_length=25)),
                ('carrying_size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ontransit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('deliveryMode', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='delivery.deliverymode')),
                ('orderNumber', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='order.ordernumberpartner')),
            ],
        ),
    ]
