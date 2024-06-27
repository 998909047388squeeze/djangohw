# Generated by Django 5.0.6 on 2024-06-27 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_categorymodel_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'verbose_name': 'Categoty', 'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(max_length=90)),
                ('title_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.newscategorymodel')),
            ],
            options={
                'verbose_name': 'New',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_name', models.CharField(max_length=80)),
                ('price', models.FloatField()),
                ('count', models.IntegerField(default=0)),
                ('descriptions', models.TextField()),
                ('image', models.FileField(upload_to='product_image')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categorymodel')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
