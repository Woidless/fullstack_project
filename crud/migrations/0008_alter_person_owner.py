# Generated by Django 4.1.2 on 2022-11-09 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crud', '0007_person_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='owner',
            field=models.ForeignKey(blank=True, max_length=100, on_delete=django.db.models.deletion.RESTRICT, related_name='person', to=settings.AUTH_USER_MODEL),
        ),
    ]
