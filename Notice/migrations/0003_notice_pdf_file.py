# Generated by Django 4.2.7 on 2023-12-11 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notice', '0002_alter_notice_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]