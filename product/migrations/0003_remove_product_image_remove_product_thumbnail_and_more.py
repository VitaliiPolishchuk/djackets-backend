# Generated by Django 4.0.2 on 2022-04-07 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
