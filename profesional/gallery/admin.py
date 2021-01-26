from django.contrib import admin

# Register your models here.
from .models import Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image','name', 'description')
    

admin.site.register(Image, ImageAdmin)
