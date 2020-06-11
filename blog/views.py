from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    template = 'blog/index.html'
    context = {}
    return render(request,template,context)
