# Generated by Django 4.2.4 on 2023-08-27 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GigsterMusicApp.applicationuser')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.CharField(max_length=255)),
                ('product_category', models.CharField(max_length=255)),
                ('product_Image', models.ImageField(upload_to='')),
                ('product_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShippingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GigsterMusicApp.applicationuser')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInShippingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShippingCart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GigsterMusicApp.shippingcart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GigsterMusicApp.orderitem')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GigsterMusicApp.orderitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GigsterMusicApp.order')),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GigsterMusicApp.product'),
        ),
    ]