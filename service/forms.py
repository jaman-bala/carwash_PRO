from django import forms
from service.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('model_car', 'number_car', 'service', 'sum', 'title', 'image',)
        widgets = {

            "model_car": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Модель машины"
                       }),
            "number_car": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Номер машины"
                       }),
            "service": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Вид услуги"
                       }),
            "sum": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Сумма"
                       }),
            "title": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Имя автомойщика"
                       }),
            "image": forms.FileInput(
                attrs={"class": "form-control",
                       "placeholder": "Фотография автомобиля"
                       }),
        }
