# Generated by Django 3.0.6 on 2020-06-04 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalk', '0007_view_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='count_views',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_typ', models.CharField(default='views', max_length=10, null=True)),
                ('totalView', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='view_count',
        ),
    ]
