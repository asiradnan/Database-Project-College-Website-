# Generated by Django 4.2.7 on 2023-12-13 01:58

import Academics.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0005_alter_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=10, validators=[Academics.models.id_validate]),
        ),
    ]
