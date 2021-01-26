from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from  django.contrib.auth.models import User
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
# Create your views here.

@login_required
def upload_image(request):
 
    if request.method == 'GET':
        return render(request, 'upload_image.html')
    elif request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            new_image = Image(
                                image = form.cleaned_data["image"],
                                name = form.cleaned_data["name"],
                                description = form.cleaned_data["description"]
                                )
            new_image.save()
            return HttpResponseRedirect('/gallery/image_gallery/')
        
        
        
def image_gallery(request):
    
    images = Image.objects.all()
    return render(request, 'image_gallery.html', {'images': images})