# Generated by Django 4.1.2 on 2022-12-26 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DishMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Введите названия блюд ')),
                ('image_url', models.URLField(max_length=5000, null=True, verbose_name='Вставье ссылку на картинку')),
                ('descriptions', models.TextField(max_length=2000, verbose_name='Описания продукта ')),
                ('recommendations', models.CharField(max_length=50, null=True, verbose_name='Рекомендуем принимать это на ')),
                ('Ingredients', models.CharField(max_length=1000, null=True, verbose_name='Введите Ингредиент продукта ')),
                ('Fats', models.CharField(max_length=100, null=True, verbose_name='Жиры продукта')),
                ('Squirrels', models.CharField(max_length=100, null=True, verbose_name='Белки продукта ')),
                ('Carbohydrates', models.CharField(max_length=100, null=True, verbose_name='Углеводы')),
                ('calories', models.CharField(max_length=100, null=True, verbose_name='Калорий')),
            ],
        ),
    ]