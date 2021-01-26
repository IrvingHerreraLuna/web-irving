from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'gallery'
gallery_patterns = [
    path('upload_image/', views.upload_image, name='upload_image'),
    path('image_gallery/', views.image_gallery, name='image_gallery')
]

#gallery_patterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




