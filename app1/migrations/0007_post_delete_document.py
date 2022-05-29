# Generated by Django 4.0.3 on 2022-05-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('cover', models.ImageField(upload_to='documents/')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]