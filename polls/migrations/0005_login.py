# Generated by Django 3.2 on 2021-04-19 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_student_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('retype_password', models.CharField(max_length=50)),
            ],
        ),
    ]