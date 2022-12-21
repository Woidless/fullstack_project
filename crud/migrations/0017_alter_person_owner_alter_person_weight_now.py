# Generated by Django 4.1.2 on 2022-12-20 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crud', '0016_rename_sex_person_gender_remove_person_allergy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='owner',
            field=models.OneToOneField(blank=True, max_length=100, on_delete=django.db.models.deletion.RESTRICT, related_name='person', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='person',
            name='weight_now',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Текущий вес'),
        ),
    ]
