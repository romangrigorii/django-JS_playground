# Generated by Django 4.0.4 on 2022-09-05 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='first',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='passenger',
            name='last',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
