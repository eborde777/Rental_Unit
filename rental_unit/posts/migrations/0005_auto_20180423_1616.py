# Generated by Django 2.0.4 on 2018-04-23 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180423_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='furnishing_details',
            field=models.CharField(max_length=200),
        ),
    ]
