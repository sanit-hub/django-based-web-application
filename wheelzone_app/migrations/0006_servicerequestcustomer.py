# Generated by Django 3.0.7 on 2021-01-23 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wheelzone_app', '0005_delete_servicerequestcustomer'),
    ]

    operations = [
        migrations.CreateModel(
            name='servicerequestcustomer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('regno', models.TextField()),
                ('location', models.TextField()),
                ('services', models.TextField()),
                ('phonenumber', models.TextField()),
                ('service_status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
