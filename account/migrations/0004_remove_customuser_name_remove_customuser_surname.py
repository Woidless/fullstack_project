# Generated by Django 4.1.2 on 2022-11-09 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_customuser_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='surname',
        ),
    ]
