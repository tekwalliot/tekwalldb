# Generated by Django 3.2.8 on 2021-10-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0013_expenses_attach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='Attach',
            field=models.FileField(blank=True, null=True, upload_to='expenses/'),
        ),
    ]
