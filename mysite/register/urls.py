from django.urls import path
from . import views

app_name = "register"


urlpatterns = [
    path('register/', views.register, name="register"),
    path('logged_out/', views.logged_out, name="logged_out"),
]
