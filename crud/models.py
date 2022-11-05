from django.db import models
from account.models import CustomUser


class Person(models.Model):
    owner = models.ForeignKey(CustomUser, max_length=100, on_delete=models.CASCADE, related_name='person')
    age =  models.DecimalField('Возраст', max_digits=10, decimal_places=2)
    height = models.DecimalField('Рост', max_digits=10, decimal_places=2)
    weight = models.DecimalField('Вес', max_digits=10, decimal_places=2)
    blood_type = models.CharField('Группа крови', max_length=10, blank=True)
    allergy = models.CharField('Аллергия', max_length=100, blank=True)
    symptoms = models.CharField('Симптомы', max_length=500, blank=True)
    disability = models.CharField('Инвалидность', max_length=100, blank=True)
    injury = models.CharField('Травма', max_length=100, blank=True)
    illness = models.CharField('Болезнь', max_length=100, blank=True)
    person_images = models.ImageField('Фотография', max_length=100, blank=True)
    

    def __str__(self) -> str:
        return f'{self.owner.name}  {self.owner.surname}  Σ(°△°|||)' 