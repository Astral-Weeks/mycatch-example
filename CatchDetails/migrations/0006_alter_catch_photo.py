# Generated by Django 4.2.6 on 2025-01-30 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatchDetails', '0005_alter_catch_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catch',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
