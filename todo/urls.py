from .views import TodoListCreate, TodoItem
from django.urls import path

urlpatterns = [
    path('', TodoListCreate.as_view()),
    path('<int:pk>/', TodoItem.as_view())
]