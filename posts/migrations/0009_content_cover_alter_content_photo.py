# Generated by Django 4.0.4 on 2022-06-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_rename_image_content_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to='media/img'),
        ),
        migrations.AlterField(
            model_name='content',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/img'),
        ),
    ]
