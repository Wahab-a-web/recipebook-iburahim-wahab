from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return HttpResponse('Hello World! This came from the index view')


class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipe_book.html'

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)




class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'
    redirect_field_name = 'recipes/list'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = '__all__'
    template_name = 'add_recipe.html'


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = '__all__'
    template_name = 'recipe.html'
    redirect_field_name = 'recipes/list'