# Generated by Django 4.1.2 on 2022-12-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0022_remove_person_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=100, null=True, verbose_name='Ник'),
        ),
    ]
