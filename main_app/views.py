from django.shortcuts import render

# Create your views here.

def home(request):
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets':widgets})