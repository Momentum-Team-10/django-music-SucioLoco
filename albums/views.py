# from _typeshed import HasFileno
# from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(
        '<h1>Home</h1>'
        '<button>Add New Movie</button>'
        )
# Create your views here.
