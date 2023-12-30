from django.shortcuts import render

# Create your views here.

from .models import *
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import *

class home(ListView):
    model=Employee
    template_name ='home.html'
    context_object_name ='data'

class Create_View(CreateView):
    model=Employee
    form_class = Employee_form
    template_name = 'create.html'
    success_url = reverse_lazy('home')


class Update_View(UpdateView):
    model=Employee
    form_class = Employee_form
    template_name = 'update.html'
    success_url = reverse_lazy('home')

class Delete_View(DeleteView):
    model=Employee
    success_url = reverse_lazy('home')

