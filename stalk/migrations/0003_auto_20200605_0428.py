# Generated by Django 3.0.6 on 2020-06-04 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalk', '0002_auto_20200605_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stalkers',
            name='ip',
            field=models.CharField(default='Unknown', max_length=60),
        ),
    ]
