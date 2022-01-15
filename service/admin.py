from django.contrib import admin
from service.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'model_car', 'number_car', 'service', 'sum', 'created')
