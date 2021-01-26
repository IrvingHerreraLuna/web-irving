from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to= 'gallery/',default='gallery/images/no-img.jpg')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
    
    
    