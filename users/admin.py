from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import forms
from . import models

class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = models.CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', 'gender'] 

admin.site.register(models.CustomUser, CustomUserAdmin)