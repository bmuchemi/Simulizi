# Generated by Django 4.2.2 on 2023-06-29 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0015_delete_stor_story_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='TEST',
        ),
    ]
