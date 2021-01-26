from django.db.models import fields
from django.shortcuts import render
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.urls.base import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile




# Create your views here.

class SingupView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    def get_success_url(self):
        return reverse_lazy('login') + '?register_ok'
    
    
    def get_form(self,form_class=None):
        form = super(SingupView, self).get_form()
        form.fields['username'].widget =  forms.TextInput(attrs={'class':'form_control mb-2','placeholder':'Nombre de registro'})
        form.fields['first_name'].widget =  forms.TextInput(attrs={'class':'form_control mb-2','placeholder':'Nombre de usuario'})
        form.fields['last_name'].widget =  forms.TextInput(attrs={'class':'form_control mb-2','placeholder':'Apellido de usuario'})
        form.fields['email'].widget =  forms.EmailInput(attrs={'class':'form_control mb-2','placeholder':'Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form_control mb-2','placeholder':'contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form_control mb-2','placeholder':' Repetir contraseña'})
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'
    
    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    
    
    
    
@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'
    
    def get_object(self):
        return self.request.user
    
    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Nuevo email'})
        return form