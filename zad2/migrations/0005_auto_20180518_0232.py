# Generated by Django 2.0.4 on 2018-05-18 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zad2', '0004_plane_places'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='start_hour',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='flight',
            name='start_minutes',
            field=models.IntegerField(default=0),
        ),
    ]
