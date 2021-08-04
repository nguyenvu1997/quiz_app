from django.db import models
from users.models import CustomUser

# Create your models here.
class Task(models.Model):
    user =  models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150)
    description= models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['complete']