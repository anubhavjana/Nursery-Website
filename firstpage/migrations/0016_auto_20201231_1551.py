# Generated by Django 3.1.4 on 2020-12-31 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstpage', '0015_cartorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorders',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cartorders',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]