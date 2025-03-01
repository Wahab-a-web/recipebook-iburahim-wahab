from django.db import models
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('ingredients', args=[str(self.name)])
    
    def __str__(self):
        return '{} ingredient'.format(self.name)        


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('ledger:recipes', args=[self.pk])

    def __str__(self):
        return 'Recipe {}'.format(self.name)


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100, default='0')  
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients',
    )