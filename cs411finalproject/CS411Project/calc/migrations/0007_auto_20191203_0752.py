# Generated by Django 2.2.7 on 2019-12-03 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_auto_20191202_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perference',
            fields=[
                ('uid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=20)),
                ('heightlowbound', models.IntegerField()),
                ('heighthighbound', models.IntegerField()),
                ('agelowbound', models.IntegerField()),
                ('agehighbound', models.IntegerField()),
                ('race', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('schoolname', models.CharField(max_length=100)),
                ('companyname', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Prefernces',
        ),
        migrations.DeleteModel(
            name='suggestions',
        ),
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
    ]
