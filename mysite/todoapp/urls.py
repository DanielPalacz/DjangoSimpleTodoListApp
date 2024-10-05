from django.urls import path
from . import views

app_name = "todoapp"


urlpatterns = [
    path('<int:pk>/', views.todoapp_list, name="todoapp_list"),
    path('', views.home, name="home"),
]
