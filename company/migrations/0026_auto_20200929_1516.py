# Generated by Django 3.1.1 on 2020-09-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0025_auto_20200927_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employ_form2',
            name='my_population',
            field=models.CharField(max_length=200),
        ),
    ]
