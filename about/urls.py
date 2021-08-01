from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('resume/', views.resume_download, name='resume'),
    path('contact/', views.contact_view, name='contact'),
]