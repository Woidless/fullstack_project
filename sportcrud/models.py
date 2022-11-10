from django.db import models
from category.models import Category

class SportCrud(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='video/', blank=True)
    descriptions = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='SportCrud')

    def __str__(self):
        return f'{self.title}'