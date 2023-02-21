from .views import TodoListCreate, TodoItem
from django.urls import path

urlpatterns = [
    path('', TodoListCreate.as_view()),
    # This is a url pattern that will match any url that has an integer in it for a the todo task.
    path('<int:pk>/', TodoItem.as_view())
]