# Generated by Django 4.1 on 2022-09-01 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0004_alter_bwc_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bwc',
            name='profile',
            field=models.ImageField(null=True, upload_to='profile'),
        ),
    ]