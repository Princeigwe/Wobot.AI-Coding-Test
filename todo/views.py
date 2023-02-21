from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsOwner

# Create your views here.


# the class responsible for creating and listing todo tasks
class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    # linking the logged in user to the created task
    def perform_create(self, serializer): 
        serializer.save(owner=self.request.user)

# the class responsible for reading, updating and deleting a todo task
class TodoItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwner,)