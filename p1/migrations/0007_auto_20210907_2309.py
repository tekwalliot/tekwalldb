# Generated by Django 3.1.1 on 2021-09-07 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0006_auto_20210907_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='Name',
            field=models.CharField(help_text='Company Name', max_length=50, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='customerdetails',
            unique_together={('Name', 'Nick_Name')},
        ),
    ]
