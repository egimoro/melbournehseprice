# Generated by Django 3.0.7 on 2020-06-10 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms', models.IntegerField(default=0)),
                ('hsetype', models.CharField(max_length=1)),
                ('price', models.FloatField(default=0)),
                ('method', models.CharField(max_length=3)),
                ('datesold', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suburb', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=4)),
                ('propertycount', models.IntegerField(default=0)),
                ('distance', models.FloatField(default=0)),
                ('council_area', models.CharField(max_length=250)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='melbournehseprice.House')),
            ],
        ),
    ]