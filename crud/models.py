from django.db import models
from account.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class Person(models.Model):
    owner = models.ForeignKey(User, 
                            unique=True,
                            max_length=100,
                            on_delete=models.RESTRICT,
                            related_name='person',
                            blank=True
                            )
    name = models.CharField('Имя',max_length=100, blank=True)
    surname = models.CharField('Фамилия' ,max_length=100, blank=True)
    age =  models.DecimalField('Возраст', max_digits=10, decimal_places=0)
    height = models.DecimalField('Рост', max_digits=10, decimal_places=0)
    weight = models.DecimalField('Вес', max_digits=10, decimal_places=0)
    sex = models.CharField('Пол', max_length=10, blank=True)
    blood_type = models.CharField('Группа крови', max_length=10, blank=True)
    allergy = models.CharField('Аллергия', max_length=100, blank=True)
    symptoms = models.CharField('Симптомы', max_length=500, blank=True)
    disability = models.CharField('Инвалидность', max_length=100, blank=True)
    injury = models.CharField('Травма', max_length=100, blank=True)
    illness = models.CharField('Болезнь', max_length=100, blank=True)
    person_images = models.ImageField(upload_to='images')

    def __str__(self) -> str:
        return f'{self.owner.email}  Σ(°△°|||)' 