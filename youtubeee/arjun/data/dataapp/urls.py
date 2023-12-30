from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home.as_view(),name='home'),
    path('create',Employee_create.as_view(),name='create'),
    path('update/<int:id>',Employee_update.as_view(),name='update'),
    path('delete/<int:id>',Employee_delete.as_view(),name='delete')

]
