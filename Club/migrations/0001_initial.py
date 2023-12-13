# Generated by Django 4.2.7 on 2023-12-05 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Academics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('club_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('established', models.DateField()),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academics.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('Member', 'Member'), ('President', 'President'), ('Vice President', 'Vice President'), ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer')], max_length=20)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Club.club')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academics.student')),
            ],
        ),
    ]