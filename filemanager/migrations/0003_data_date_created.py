# Generated by Django 2.1 on 2019-01-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0002_remove_data_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='date_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]