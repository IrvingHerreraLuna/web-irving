"""profesional URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import Pattern
from django.contrib import admin
from django.urls import path, include
# cargar las urls de pages
from pages.urls import pages_patterns
from Profiles.urls import profiles_patterns
from gallery.urls import gallery_patterns
# importar  la config desde settngs 
from django.conf import settings

from messenger.urls import messenger_patterns


urlpatterns = [
    path('', include('core.urls')),
    path('pages/',include(pages_patterns)),
    path('admin/', admin.site.urls),

    # path de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('profiles/', include(profiles_patterns)),
    path('messenger/', include(messenger_patterns)),
    path('gallery/', include(gallery_patterns)),

] 

#if settings.DEBUG:
#    from django.conf.urls.static import static
#    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
    
#from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)