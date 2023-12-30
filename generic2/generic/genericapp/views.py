from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import *
from .forms import *

class EmployeeListview(ListView):
    model=Employee
    template_name='home.html'
    context_object_name = 'Employee'


class EmployeeCreateview(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'create.html'
    success_url = reverse_lazy('list')

class EmployeeUpdateview(UpdateView):
    model =Employee
    form_class = EmployeeForm
    template_name = 'update.html'
    success_url = reverse_lazy('list')

class EmployeeDeleteview(DeleteView):
    model = Employee
    success_url = reverse_lazy('list')






