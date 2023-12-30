from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django .views import View

from .models import *
from .forms import *
class home(View):
    def get(self,request):
        data=Employee.objects.all()
        return render(request,'home.html',{"data":data})

class Employee_create(View):
    def get(self,request):
        form=Employee_form()
        return render(request,'create.html',{"form":form})

    def post(self,request):
        form=Employee_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
        else:
            return redirect(reverse_lazy('create'))


class Employee_update(View):
    def get(self,request,id):
        employee=Employee.objects.get(id=id)
        form=Employee_form(instance=employee)
        return render(request, 'update.html', {"form": form})

    def post(self,request,id):
        employee=Employee.objects.get(id=id)
        form =Employee_form(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
        else:
            return redirect(reverse_lazy('update'))

class Employee_delete(View):
    def get(self,request,id):
        employee=Employee.objects.get(id=id)
        employee.delete()
        return redirect(reverse_lazy('home'))

