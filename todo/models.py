from django.db import models
from account.models import CustomUser

# Create your models here.


class Todo(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.name