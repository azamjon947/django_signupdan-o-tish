from django.shortcuts import redirect, render, reverse
from django.views import generic
from .form import Registration
# from .models import *


class Home(generic.TemplateView):
    template_name = 'index.html'

    
class Register(generic.CreateView):
    template_name = 'signup.html'   
    form_class = Registration

    
    def get_succes_url(self):
        return reverse('django:home')


