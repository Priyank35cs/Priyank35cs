# Generated by Django 2.2 on 2019-04-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='ecom/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.ImageField(default='', max_length=50, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(default=0),
        ),
    ]
