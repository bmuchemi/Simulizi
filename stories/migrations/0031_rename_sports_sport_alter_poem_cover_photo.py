# Generated by Django 4.2.2 on 2023-09-15 10:17

from django.db import migrations, models
import stories.models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0030_alter_sports_desk_image_alter_story_cover_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sports',
            new_name='Sport',
        ),
        migrations.AlterField(
            model_name='poem',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to=stories.models.poem_cover_upload_path),
        ),
    ]