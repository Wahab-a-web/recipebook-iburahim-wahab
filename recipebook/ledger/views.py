from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    return HttpResponse('Hello World! This came from the index view')

class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipe_book.html'
    

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'
    redirect_field_name = 'recipes/list'
