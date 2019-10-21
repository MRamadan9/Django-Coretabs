# Generated by Django 2.0.2 on 2018-06-04 19:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ordering_users',
            field=models.ManyToManyField(related_name='ordered_products', through='orders.Order', to=settings.AUTH_USER_MODEL),
        ),
    ]