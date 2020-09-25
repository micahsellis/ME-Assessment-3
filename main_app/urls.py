from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('widgets/add_widget/', views.add_widget, name='add_widget'),
    path('widgets/<int:widget_id>/delete/', views.widget_delete, name='widget_delete')
]
