# Generated by Django 3.0.7 on 2021-03-05 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wheelzone_app', '0013_parts_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='parts',
            name='date',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]