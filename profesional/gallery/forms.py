from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields =['image','name','description']
        
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'name': forms.TextInput(attrs={'class':'form-control-file mt-3','placeholder':'Nombre de imagen'}),
            'description': forms.Textarea(attrs={'class':'form-control-file mt-3','placeholder':'descripción'})
        }