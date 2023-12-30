from django.urls import path
from .views import *

urlpatterns = [
    path('', TeacherListView.as_view(), name='list'),
    path('create', TeacherCreateView.as_view(), name='create'),
    path('update/<int:pk>', TeacherUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TeacherDeleteView.as_view(), name='delete'),
]
