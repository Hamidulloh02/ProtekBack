# Generated by Django 4.2.7 on 2023-12-18 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_brand_alter_productclass_name_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
