from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'index.html', {'widgets': widgets, 'widget_form': widget_form})
    
def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('home')