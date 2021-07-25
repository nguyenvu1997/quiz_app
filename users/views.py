from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from .models import CustomUser


# Create your views here.
class UserCreate(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('home')

class UserUpdate(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('home')

# def home(request):
#     return render(request, 'home.html')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'