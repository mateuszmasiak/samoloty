# Generated by Django 2.0.4 on 2018-06-01 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zad2', '0016_planecrew'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PlaneCrews',
        ),
        migrations.AddField(
            model_name='planecrew',
            name='crew_id',
            field=models.IntegerField(default=1),
        ),
    ]
