from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """TODO: Docstring for index.

    :request: TODO
    :returns: TODO

    """
    return HttpResponse("Hello, world. You're at the polls index.")
