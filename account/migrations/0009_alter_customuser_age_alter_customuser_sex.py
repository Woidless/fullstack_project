# Generated by Django 4.1.2 on 2022-12-15 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_customuser_age_alter_customuser_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sex',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
