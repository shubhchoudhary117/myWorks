# Generated by Django 4.0 on 2022-04-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultdatabase',
            name='RollNo',
            field=models.CharField(max_length=500),
        ),
    ]
