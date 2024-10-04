from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("<h1>Starting simple todo list tutorial</h1>")


def v1(request):
    return HttpResponse("<h1>v1 page</h1>")

def v1_detail_int(request, num):
    return HttpResponse(f"<h1>v1_detail_int page:<br>- num: {num}</h1>")


def v1_detail_str(request, num):
    return HttpResponse(f"<h1>v1_detail_int page:<br>- text: {num}</h1>")



def index_json(request):
    return JsonResponse({"message": "Starting simple todo list tutorial"})
