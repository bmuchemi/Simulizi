# Generated by Django 4.2.2 on 2023-07-01 01:14

from django.db import migrations, models
import stories.models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0024_alter_story_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to=stories.models.story_cover_upload_path),
        ),
    ]
