# Generated by Django 3.2.8 on 2021-10-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0015_alter_expenses_attach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='Attach',
            field=models.FileField(blank=True, upload_to='expenses/'),
        ),
    ]
