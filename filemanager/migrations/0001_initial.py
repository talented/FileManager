# Generated by Django 2.1 on 2019-01-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('data_id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.FileField(max_length=255, null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
