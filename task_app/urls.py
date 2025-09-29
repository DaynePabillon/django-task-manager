from django.urls import path
from . import views

app_name = 'task_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/update/', views.update_task_status, name='update_task_status'),
]
