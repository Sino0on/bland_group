# Generated by Django 4.0.5 on 2022-08-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_product_subcategory_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gLTF',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
