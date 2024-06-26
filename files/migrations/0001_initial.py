# Generated by Django 5.0.6 on 2024-06-18 22:56

import files.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependencies', models.JSONField(blank=True, default=list)),
                ('pic', models.ImageField(blank=True, default='no-pic.png', upload_to=files.models.pic_path, verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Vid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependencies', models.JSONField(blank=True, default=list)),
                ('vid', models.FileField(upload_to=files.models.vid_path)),
            ],
        ),
    ]
