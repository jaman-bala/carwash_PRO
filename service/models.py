from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Мойщик")
    model_car = models.CharField(max_length=255, verbose_name="Модель машины")
    number_car = models.CharField(max_length=255, verbose_name="Номер машины")
    service = models.CharField(max_length=255, verbose_name="Вид услуги")
    sum = models.CharField(max_length=255, verbose_name="Сумма")
    image = models.ImageField(upload_to='media', null=True, default='media/car_icon.png')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Данные авто"
        verbose_name_plural = "Добавить"

    def __str__(self):
        return self.title


