from django.db import models

class DishMenu(models.Model):
    title = models.CharField('Введите названия блюд ', max_length=100, unique=True)
    # image = models.ImageField('Вставьте картинку ', upload_to='DishFiles', null=True)
    image_url = models.URLField('Вставье ссылку на картинку' , max_length=5000, null=True, blank=True)
    descriptions = models.TextField('Описания продукта ', max_length=2000)
    recommendations = models.CharField('Рекомендуем принимать это на ', max_length=50, null=True, blank=True)
    Ingredients = models.CharField('Введите Ингредиент продукта ', max_length=1000, null=True, blank=True)
    Fats = models.CharField('Жиры продукта', max_length=100, null=True, blank=True)
    Squirrels = models.CharField('Белки продукта ', max_length=100, null=True, blank=True)
    Carbohydrates = models.CharField('Углеводы', max_length=100, null=True, blank=True)
    calories = models.CharField('Калорий', max_length=100, null=True, blank=True)

    def __str__(self):
        return f' {self.title} ^_^'