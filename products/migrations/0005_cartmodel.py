# Generated by Django 5.0.6 on 2024-06-27 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_newscategorymodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_product_quantity', models.IntegerField(default=0)),
                ('user_add_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productmodel')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
    ]
