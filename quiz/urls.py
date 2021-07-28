from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuizTemplateView.as_view(), name = 'quiz'),
    path('result/', views.QuizResult, name = 'quiz_result'),
    path('quiz_list/', views.QuizList.as_view(), name = 'quiz_list'),
    path('<str:pk>/', views.QuizDetail.as_view(), name = 'quiz_detail'),
]
