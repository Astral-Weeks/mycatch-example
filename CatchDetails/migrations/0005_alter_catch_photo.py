# Generated by Django 4.2.6 on 2025-01-30 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatchDetails', '0004_catch_photo_alter_catch_tag_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catch',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
