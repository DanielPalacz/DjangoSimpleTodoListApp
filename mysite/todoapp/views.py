from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TodoItem, TodoList


def todoapp_list(request, pk):
    todolist_object = TodoList.objects.get(id=pk)
    return render(request, "todoapp/list.html", {"todolist_object": todolist_object})


def home(request):
    return render(request, "todoapp/home.html", {"name": "test"})
