# Generated by Django 3.0.7 on 2020-06-16 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melbournehseprice', '0004_auto_20200616_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='houses',
            new_name='house',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='propertycount',
            new_name='property_count',
        ),
        migrations.RemoveField(
            model_name='location',
            name='council_area',
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='location',
            name='suburb',
            field=models.CharField(max_length=200),
        ),
    ]