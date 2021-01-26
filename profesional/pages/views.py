#from django.shortcuts import render, get_object_or_404, get_list_or_40
from django.views.generic.list import  ListView
from .models import Page
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from .forms import PageForm
from django.shortcuts import redirect

# Create your views here.


class StaffRequiredMixin(object): 
    # esta clase mixin requerira que el usuario sea miembro del grupo staff
    
    @method_decorator(staff_member_required)
    def dispatch(self, request,*args,**kwargs):
        return super(StaffRequiredMixin, self).dispatch(request,*args,**kwargs)



class PagesListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page
    
@method_decorator(staff_member_required,name='dispatch')
class PagesCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')
    
    
    #def get_success_url(self):
    #    return reverse('pages:pages')

@method_decorator(staff_member_required,name='dispatch')    
class PageUpdate(UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'
    def get_success_url(self):
       return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
   
@method_decorator(staff_member_required,name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')