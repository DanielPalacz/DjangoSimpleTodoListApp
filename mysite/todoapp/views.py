from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import TodoItem, TodoList
from .forms import CreateTodoListForm

def todoapp_list(request, pk):
    todolist_object = TodoList.objects.get(id=pk)

    if request.method == "POST":
        print("request.POST:", request.POST)
        if request.POST.get("update"):
            for item in todolist_object.todoitem_set.all():
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif request.POST.get("NewItem"):
            txt = request.POST.get("newValue")
            if len(txt) > 2:
                todolist_object.todoitem_set.create(text=txt, complete=False)
            elif not len(txt):
                print(f"Text '{txt}' is empty phrase did not pass validation. Invalid input.")
            else:
                print(f"Text '{txt}' did not pass validation. Invalid input.")

    return render(request, "todoapp/list.html", {"todolist_object": todolist_object})


def home(request):
    todolists = TodoList.objects.all()
    return render(request, "todoapp/home.html", {"todolists": todolists})


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
