# Generated by Django 3.0.3 on 2020-06-04 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stalkersIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('ip', models.CharField(default='Unkown', max_length=60)),
                ('useragent', models.CharField(default='Unknown', max_length=100)),
            ],
        ),
    ]
