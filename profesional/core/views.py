from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = 'core/home.html'
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Hola, primera vists de clase o vista basada en clases'
        return context
    
    def get(self,request):
        return render(request,self.template_name,{'title':'Hola, primera vists de clase o vista basada en Clases'})
    
class SamplePageView(TemplateView):
    template_name = 'core/sample.html'