# Generated by Django 3.2.3 on 2021-10-19 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.CharField(blank=True, choices=[('MoCo', 'Mobiles & Computers'), ('TVAE', 'TV, Appliances & Electronics'), ('MFas', "Men's Fashion"), ('WFas', "Women's Fashion"), ('Book', 'Books'), ('Kitc', 'Kitchen')], max_length=4)),
                ('name', models.CharField(max_length=255)),
                ('short', models.CharField(max_length=4)),
            ],
        ),
    ]