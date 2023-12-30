from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *
from .forms import *


class TeacherListView(ListView):
    model = Teacher
    template_name = 'index.html'
    context_object_name = 'teachers'


class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'create.html'
    success_url = reverse_lazy('list')


class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'update.html'
    success_url = reverse_lazy('list')


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('list')
