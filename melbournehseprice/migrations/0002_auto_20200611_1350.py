# Generated by Django 3.0.7 on 2020-06-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melbournehseprice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='datesold',
            field=models.DateField(verbose_name='%d/%m/%Y'),
        ),
    ]
