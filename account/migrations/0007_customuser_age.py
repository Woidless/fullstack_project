# Generated by Django 4.1.2 on 2022-12-15 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_customuser_person_status_customuser_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
