# Generated by Django 2.2.7 on 2019-12-05 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0017_delete_suggestions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=10)),
                ('suggested', models.CharField(max_length=10)),
            ],
            options={
                'unique_together': {('uid', 'suggested')},
            },
        ),
    ]