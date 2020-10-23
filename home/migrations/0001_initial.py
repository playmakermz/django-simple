# Generated by Django 3.0.10 on 2020-09-28 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('tipe', models.CharField(max_length=100)),
                ('ukuran', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('myfile', models.FileField(upload_to='file/%w')),
            ],
        ),
    ]
