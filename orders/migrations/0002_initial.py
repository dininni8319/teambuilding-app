# Generated by Django 3.2.9 on 2021-12-09 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='priceByQuantity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.pricebyquantity', verbose_name='Price by quantity'),
        ),
    ]
