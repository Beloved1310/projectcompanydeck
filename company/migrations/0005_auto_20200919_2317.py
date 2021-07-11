# Generated by Django 3.1.1 on 2020-09-19 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_employer_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer_form',
            name='amount1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employer_form',
            name='amount2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employer_form',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='employer_form',
            name='phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterModelTable(
            name='employer_form',
            table='web_Employer_Form',
        ),
    ]