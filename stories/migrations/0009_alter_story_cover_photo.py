# Generated by Django 4.2.2 on 2023-06-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0008_alter_story_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to='./static/story_covers'),
        ),
    ]
