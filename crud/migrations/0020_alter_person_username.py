# Generated by Django 4.1.2 on 2022-12-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0019_person_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(default=(), max_length=100),
        ),
    ]
