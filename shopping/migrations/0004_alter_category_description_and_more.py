# Generated by Django 4.0.3 on 2022-06-30 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_product_delete_product_section_remove_category_cart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_description',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_keywords',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_title',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=150),
        ),
    ]
