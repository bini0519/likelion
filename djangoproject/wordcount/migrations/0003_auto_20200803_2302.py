# Generated by Django 3.0.8 on 2020-08-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordcount', '0002_auto_20200801_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designer',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]