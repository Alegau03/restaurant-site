from django.urls import path
from . import views
from django.contrib import admin
urlpatterns=[
    path('', views.rolls,name='home'),
    path('contattaci',views.contattaci,name='contattaci'),
    path('compra',views.compra,name="compra")
]