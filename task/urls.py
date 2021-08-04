from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name= 'tasks'),
    path('create', views.TaskCreate.as_view(), name= 'task_create'),
    path('<int:pk>', views.TaskDetail.as_view(), name= 'task_detail'),
    path('delete/<int:pk>', views.TaskDelete.as_view(), name= 'task_delete'),
    path('edit/<int:pk>', views.TaskUpdate.as_view(), name= 'task_edit'),
]
