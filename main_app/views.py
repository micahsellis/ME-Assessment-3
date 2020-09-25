from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets':widgets})