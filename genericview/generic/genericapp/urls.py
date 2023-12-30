from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',home.as_view(),name='home'),
    path('create',Create_View.as_view(),name='create'),
    path('update/<int:pk>',Update_View.as_view(),name='update'),
    path('delete/<int:pk>',Delete_View.as_view(),name='delete'),


]
