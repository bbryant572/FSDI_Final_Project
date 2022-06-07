# Generated by Django 4.0.4 on 2022-06-05 17:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/img'),
            preserve_default=False,
        ),
    ]
