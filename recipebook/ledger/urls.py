from django.urls import path

from .views import index, RecipeDetailView, RecipesListView

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', RecipesListView.as_view(), name='recipes/list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
]

app_name = 'ledger'