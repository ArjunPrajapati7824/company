from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views import View


# Create your views here.

class Index(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        contex = {"teachers": teachers}
        return render(request, 'index.html', contex)


class TeacherCreate(View):
    def get(self, request):
        form = TeacherForm()
        return render(request, 'create.html', {"form": form})

    def post(self, request):
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('index'))
        else:
            return redirect(reverse_lazy('create'))


class TeacherUpdate(View):
    def get(self, request, **kwargs):
        teacher = Teacher.objects.get(id=kwargs['id'])
        form = TeacherForm(instance=teacher)
        return render(request, 'update.html', {'form': form})

    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('index'))
        else:
            return redirect(reverse_lazy('update'))


class TeacherDelete(View):
    def get(self, request, **kwargs):
        teacher = Teacher.objects.get(id=kwargs['id'])
        teacher.delete()
        return redirect(reverse_lazy('index'))
