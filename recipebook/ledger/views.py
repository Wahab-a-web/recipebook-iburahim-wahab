from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

# Create your views here.

def index(request):
    return HttpResponse('Hello World! This came from the index view')

class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipe_book.html'
    

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'    