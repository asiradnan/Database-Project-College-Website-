# Generated by Django 4.2.7 on 2023-12-12 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notice', '0003_notice_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(max_length=10000),
        ),
    ]
