from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Мойщик")
    model_car = models.CharField(max_length=255, verbose_name="Модель машины")
    number_car = models.CharField(max_length=255, verbose_name="Номер машины")
    service = models.CharField(max_length=255, verbose_name="Вид услуги")
    sum = models.CharField(max_length=255, verbose_name="Сумма")
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Данные авто"
        verbose_name_plural = "Добавить"

    def __str__(self):
        return self.title


class Icon(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(upload_to='media', null=True, default='media/')

    class Meta:
        verbose_name = "Название"
        verbose_name_plural = "Иконка"

    def __str__(self):
        return self.title
