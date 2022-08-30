# Generated by Django 4.1 on 2022-08-30 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spav', '0002_flashnews_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashnews',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='datetime'),
        ),
        migrations.AlterField(
            model_name='flashnews',
            name='newsFile',
            field=models.FileField(blank=True, null=True, upload_to='news'),
        ),
        migrations.AlterField(
            model_name='flashnews',
            name='newsLink',
            field=models.URLField(blank=True, null=True),
        ),
    ]
