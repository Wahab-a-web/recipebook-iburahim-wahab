from django.urls import path

from .views import index, recipes, recipe1, recipe2

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipes, name='recipes/list'),
    path('recipe/1', recipe1, name='recipe/1'),
    path('recipe/2', recipe2, name='recipe/2'),
]

app_name = 'ledger'