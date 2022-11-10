from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Shop(models.Model):
    title = models.CharField(max_length=30, unique=True)
    photo = models.ImageField(upload_to='shop_photo')
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField('Возраст', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.title}'