# Generated by Django 4.2.2 on 2023-06-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0021_alter_author_profile_image_alter_poem_cover_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='cover_photo',
            field=models.ImageField(upload_to='images/story_covers'),
        ),
    ]
