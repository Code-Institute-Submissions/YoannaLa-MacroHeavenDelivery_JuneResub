# Generated by Django 3.2 on 2022-02-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_featured_image_product_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]