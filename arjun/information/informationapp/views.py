from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from .forms import EmployeeForm
from .models import *

# Create your views here.
def home(request):
    employee = Employee.objects.all()
    # for i in employee:
    #     print(i.name)
    return render(request, 'home.html',{"employee":employee})


def employee_create(request):
    form=EmployeeForm()
    if request.method == "POST":
        form= EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
        else:
            return redirect(reverse_lazy('create'))

    return render(request,'create.html',{'form':form})

def employee_update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(instance=employee)
    if request.method == "POST":
        form= EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
        else:
            return redirect(reverse_lazy('update'))
    return render(request,'update.html',{'form':form})

def employee_delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect(reverse_lazy('home'))




