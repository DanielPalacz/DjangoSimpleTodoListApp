from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import TodoItem, TodoList
from .forms import CreateTodoListForm

def todoapp_list(request, pk):
    todolist_object = TodoList.objects.get(id=pk)
    return render(request, "todoapp/list.html", {"todolist_object": todolist_object})


def home(request):
    return render(request, "todoapp/home.html", {"name": "test"})


def create(request):
    if request.method == "POST":
        form = CreateTodoListForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            todolist = TodoList(name=name)
            todolist.save()
            return HttpResponseRedirect(f"/{todolist.id}/")
    else:
        form = CreateTodoListForm()
    return render(request, "todoapp/create.html", {"form": form})
