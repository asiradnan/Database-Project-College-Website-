# Generated by Django 4.2.7 on 2023-12-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
