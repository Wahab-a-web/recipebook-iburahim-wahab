from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, RecipeDetailView, RecipesListView

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', RecipesListView.as_view(), name='recipes/list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
app_name = 'ledger'
