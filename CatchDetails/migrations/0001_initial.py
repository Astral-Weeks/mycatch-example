# Generated by Django 4.2.6 on 2025-01-30 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subspecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subspecies_name', models.CharField(max_length=255)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CatchDetails.species')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=255)),
                ('tackle', models.CharField(max_length=255)),
                ('licensenumber', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Catch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField(blank=True, null=True)),
                ('length_guessed', models.BooleanField(default=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('weight_guessed', models.BooleanField(default=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('river', models.CharField(blank=True, max_length=255, null=True)),
                ('tag_status', models.CharField(choices=[(1, 'Tagged'), (2, 'Untagged'), (3, 'Newly Tagged Today'), (4, 'Not Given')], default=4, max_length=4)),
                ('taken_or_released_status', models.CharField(choices=[(1, 'Taken'), (2, 'Released'), (3, 'Not Given')], default=3, max_length=4)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CatchDetails.species')),
                ('subspecies', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CatchDetails.subspecies')),
            ],
        ),
    ]
