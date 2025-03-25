from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, RecipeDetailView, RecipesListView, RecipeCreateView, RecipeUpdateView

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', RecipesListView.as_view(), name='recipes/list'),
    path('recipe/<int:pk>', RecipeUpdateView.as_view(), name='recipe-detail'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe-add'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
app_name = 'ledger'
