# Generated by Django 4.2.2 on 2023-07-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordernumberpartner',
            name='total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
