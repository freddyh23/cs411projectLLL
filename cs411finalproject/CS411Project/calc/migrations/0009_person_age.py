# Generated by Django 2.2.7 on 2019-12-03 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0008_suggestions'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
