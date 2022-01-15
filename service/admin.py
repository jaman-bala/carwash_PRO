from django.contrib import admin
from service.models import Post, Icon

admin.site.register(Icon)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'model_car', 'number_car', 'service', 'sum', 'created')


