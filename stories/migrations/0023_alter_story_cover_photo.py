# Generated by Django 4.2.2 on 2023-06-30 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0022_alter_story_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='cover_photo',
            field=models.ImageField(upload_to='images/story_covers/'),
        ),
    ]
