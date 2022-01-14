from django.urls import path
from service.views import index

urlpatterns = [
   path('', index, name='index'),
]