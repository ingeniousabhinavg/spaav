# Generated by Django 4.1 on 2022-09-01 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0002_bwc'),
    ]

    operations = [
        migrations.AddField(
            model_name='bwc',
            name='profile',
            field=models.ImageField(null=True, upload_to='bwc/profile'),
        ),
    ]