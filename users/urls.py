from django.urls import path
from . import views

urlpatterns = [
    # path('signup/', views.UserCreate.as_view(), name = 'signup'),
    # path('', views.home, name = 'home'),
    path('edit/<int:pk>/', views.UserUpdate.as_view(), name = 'edit'),
    path('signup/', views.SignUpView.as_view(), name='signup')
]