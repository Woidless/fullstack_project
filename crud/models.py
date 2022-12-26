from django.db import models
from account.models import CustomUser
from django.contrib.auth import get_user_model
from account.models import CustomUser

all_user = CustomUser.objects.all()
User = get_user_model()

class Person(models.Model):
    owner = models.ForeignKey(User,
                            unique=True,
                            max_length=100,
                            on_delete=models.CASCADE,
                            related_name='person',
                            blank=True,
                            )
    username = models.CharField('Ник', max_length=100, null=True)
    age =  models.DecimalField('Возраст', max_digits=10, decimal_places=0)
    height = models.DecimalField('Рост', max_digits=10, decimal_places=0)
    weight_now = models.DecimalField('Текущий вес', max_digits=10, decimal_places=0)
    weight_want = models.DecimalField('Желаемый вес', max_digits=10, decimal_places=0)
    gender = models.CharField('Пол', max_length=10, blank=True)
    massa = models.DecimalField('Масса', max_digits=10, decimal_places=2)


    def __str__(self) -> str:
        return f'{self.owner.email} Σ(°△°|||)' 
