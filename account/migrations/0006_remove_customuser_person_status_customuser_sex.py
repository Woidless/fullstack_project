# Generated by Django 4.1.2 on 2022-12-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_customuser_person_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='person_status',
        ),
        migrations.AddField(
            model_name='customuser',
            name='sex',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
