# Generated by Django 2.2.6 on 2019-10-29 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='companyName',
            field=models.CharField(default='N/A', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='height',
            field=models.CharField(default='N/A', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='location',
            field=models.CharField(default='N/A', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='schoolName',
            field=models.CharField(default='N/A', max_length=20),
            preserve_default=False,
        ),
    ]