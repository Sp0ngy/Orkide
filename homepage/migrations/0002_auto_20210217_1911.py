# Generated by Django 2.2.5 on 2021-02-17 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='header_image',
            field=models.ImageField(height_field=200, null=True, upload_to=None, width_field=300),
        ),
    ]