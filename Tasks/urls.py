from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import create_task,home,detail_task,delete_task,update_task

urlpatterns = [
    path('',home, name='home-view'),
    path('create_task/',create_task, name='create-task-view'),
    path('detail_task/',detail_task, name='detail-task-view'),
    path('delete_task/<int:pk>/',delete_task, name='delete-task-view'),
    path('update_task/<int:pk>/',update_task, name='update-task-view'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)