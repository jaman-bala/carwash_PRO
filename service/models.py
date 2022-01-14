from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Оператор")
    model_car = models.CharField(max_length=255, verbose_name="Модель машины")
    number_car = models.CharField(max_length=255, verbose_name="Номер машины")
    sum = models.CharField(max_length=255, verbose_name="Сумма")
    image = models.ImageField(upload_to='media')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Данные авто"
        verbose_name_plural = "Добавить"

    def __str__(self):
        return self.title


