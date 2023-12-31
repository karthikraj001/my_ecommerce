# Generated by Django 4.0.3 on 2022-06-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='get_file_path')),
                ('cart', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=48, verbose_name='fa fa-star')),
            ],
        ),
        migrations.AlterField(
            model_name='product_section',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='get_file_path'),
        ),
    ]
