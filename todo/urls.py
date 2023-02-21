from .views import TodoListCreate
from django.urls import path

urlpatterns = [
    path('', TodoListCreate.as_view())
]