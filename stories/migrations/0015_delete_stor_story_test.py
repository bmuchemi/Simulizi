# Generated by Django 4.2.2 on 2023-06-29 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0014_stor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stor',
        ),
        migrations.AddField(
            model_name='story',
            name='TEST',
            field=models.TextField(blank=True),
        ),
    ]
