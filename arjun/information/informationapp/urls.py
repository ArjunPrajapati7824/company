from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('create',employee_create,name='create'),
    path('update/<int:id>',employee_update,name='update'),
    path('delete/<int:id>',employee_delete,name='delete')

]