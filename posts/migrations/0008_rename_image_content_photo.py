# Generated by Django 4.0.4 on 2022-06-15 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_content_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='image',
            new_name='photo',
        ),
    ]
