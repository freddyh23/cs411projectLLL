# Generated by Django 2.2.6 on 2019-11-01 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_company_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='companyName',
            new_name='companyname',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='firstName',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='lastName',
            new_name='lastname',
        ),
        migrations.RemoveField(
            model_name='company',
            name='companyName',
        ),
        migrations.RemoveField(
            model_name='person',
            name='schoolName',
        ),
        migrations.RemoveField(
            model_name='school',
            name='schoolName',
        ),
        migrations.AddField(
            model_name='company',
            name='companyname',
            field=models.CharField(default='N/A', max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='schoolname',
            field=models.CharField(default='N/A', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='schoolname',
            field=models.CharField(default='N/A', max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='industry',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]
