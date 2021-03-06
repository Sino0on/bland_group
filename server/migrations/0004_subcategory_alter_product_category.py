# Generated by Django 4.0.5 on 2022-07-19 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_alter_orderfiz_options_alter_orderur_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.category')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.subcategory'),
        ),
    ]
