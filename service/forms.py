from django import forms
from service.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'model_car', 'number_car', 'sum', 'image',)
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Имя оператора"
                       }),
            "model_car": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Модель машины"
                       }),
            "number_car": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Номер машины"
                       }),
            "sum": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Сумма"
                       }),
            "image": forms.FileInput(
                attrs={"class": "form-control",
                       "placeholder": "Фотография автомобиля"
                       }),
        }
