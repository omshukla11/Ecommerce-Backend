# Generated by Django 3.2.3 on 2021-10-05 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_instock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='instock',
            field=models.IntegerField(),
        ),
    ]
