# Generated by Django 4.2.16 on 2024-12-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0004_alter_product_mrp_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/'),
        ),
    ]