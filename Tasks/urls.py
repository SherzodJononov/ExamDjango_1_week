from django.urls import path
from .views import create_task,home,detail_task,delete_task

urlpatterns = [
    path('',home, name='home-view'),
    path('create_task/',create_task, name='create-task-view'),
    path('detail_task/',detail_task, name='detail-task-view'),
    path('delete_task/<int:pk>/',delete_task, name='delete-task-view'),
]
