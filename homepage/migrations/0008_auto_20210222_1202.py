# Generated by Django 2.2.5 on 2021-02-22 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20210218_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='reference',
            field=models.URLField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]