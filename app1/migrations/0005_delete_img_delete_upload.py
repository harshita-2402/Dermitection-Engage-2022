# Generated by Django 4.0.3 on 2022-05-27 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_img_upload'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Img',
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
    ]