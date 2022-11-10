# Generated by Django 4.1.2 on 2022-11-09 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crud', '0012_person_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.ForeignKey(blank=True, max_length=100, on_delete=django.db.models.deletion.RESTRICT, related_name='status', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]