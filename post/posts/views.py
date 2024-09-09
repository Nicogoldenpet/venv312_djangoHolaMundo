from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class HomePageView(ListView): #Mostraremos los posts en forma de lista (Más tarde se puede editar)
    model = Post
    template_name = "home.html"