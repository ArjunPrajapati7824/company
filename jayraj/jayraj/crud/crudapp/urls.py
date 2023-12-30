from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('create', TeacherCreate.as_view(), name='create'),
    path('update/<int:id>', TeacherUpdate.as_view(), name='update'),
    path('delete/<int:id>', TeacherDelete.as_view(), name='delete'),
]
