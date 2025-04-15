from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('add-task/', views.add_task, name='add_task'),  
    # Add this line for adding tasks
    path('delete/<int:task_id>/', views.delete_task, name='delete'),
    path('complete/<int:task_id>/', views.complete_task, name='complete'),
    path('edit/<int:task_id>/', views.edit_task, name='edit'),

]