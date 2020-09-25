from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    widgets = Widget.objects.all()
    widget_total = 0
    for widget in widgets:
        widget_total += widget.quantity
    widget_form = WidgetForm()
    return render(request, 'index.html', {'widgets': widgets, 'widget_form': widget_form, 'widget_total':widget_total})
    
def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('home')

def widget_delete(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    return redirect('home')
