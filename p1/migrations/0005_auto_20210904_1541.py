# Generated by Django 3.1.1 on 2021-09-04 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0004_auto_20210904_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workprogress',
            old_name='CompanyName',
            new_name='Company_Name',
        ),
        migrations.RenameField(
            model_name='workprogress',
            old_name='OtherInfo',
            new_name='Other_Info',
        ),
        migrations.RenameField(
            model_name='workprogress',
            old_name='UpdateDate',
            new_name='Update_Date',
        ),
        migrations.RenameField(
            model_name='workprogress',
            old_name='WorkProgress',
            new_name='Work_Progress',
        ),
    ]
