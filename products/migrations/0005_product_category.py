# Generated by Django 3.2.3 on 2021-10-07 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('Elec', 'Electronics'), ('Fash', 'Fashion')], max_length=4),
        ),
    ]