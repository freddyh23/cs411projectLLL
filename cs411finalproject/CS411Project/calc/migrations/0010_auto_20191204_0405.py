# Generated by Django 2.2.7 on 2019-12-04 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0009_person_age'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Perference',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Suggestions',
        ),
    ]
