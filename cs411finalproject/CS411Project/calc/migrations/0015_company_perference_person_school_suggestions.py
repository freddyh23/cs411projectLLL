# Generated by Django 2.2.7 on 2019-12-04 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0014_users_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companyname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('industry', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
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
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('height', models.IntegerField()),
                ('race', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('schoolname', models.CharField(max_length=100)),
                ('companyname', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('schoolname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=25)),
                ('conference', models.CharField(max_length=25)),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('uid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('suggested', models.CharField(max_length=10)),
            ],
        ),
    ]