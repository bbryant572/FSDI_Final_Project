from django.contrib import admin
from .models import Content, Image


# class ContentAdmin(admin.ModelAdmin):
#     list_display = ('title',)


admin.site.register(Content)
admin.site.register(Image)
