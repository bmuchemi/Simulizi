# Generated by Django 4.2.2 on 2023-06-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_alter_story_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='cover_photo',
            field=models.ImageField(blank=True, default='https://images.unsplash.com/photo-1686548812883-9d3777f4c137?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHx8&auto=format&fit=crop&w=500&q=60', upload_to='static/story_covers/'),
        ),
    ]
