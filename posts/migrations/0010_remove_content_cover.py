# Generated by Django 4.0.4 on 2022-06-15 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_content_cover_alter_content_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='cover',
        ),
    ]
