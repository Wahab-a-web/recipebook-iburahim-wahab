from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient


class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage
    list_display = ['recipe', 'recipe_image']


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)