# Generated by Django 5.0 on 2024-02-08 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calapp', '0008_calmodel_img_calmodel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calmodel',
            name='img',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
