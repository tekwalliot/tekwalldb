# Generated by Django 3.1.1 on 2021-09-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0008_auto_20210907_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Is_Completed',
            field=models.BooleanField(default=False, help_text='tick if completed'),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='Nick_Name',
            field=models.CharField(help_text='Company Nick Name', max_length=20, null=True, unique=True),
        ),
    ]
