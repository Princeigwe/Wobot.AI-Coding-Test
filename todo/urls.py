from .views import TodoCreate, TodoItem, TodoList
from django.urls import path

urlpatterns = [
    path('', TodoCreate.as_view()),
    path('list/', TodoList.as_view()),
    # This is a url pattern that will match any url that has an integer in it for a the todo task.
    path('<int:pk>/', TodoItem.as_view())
]