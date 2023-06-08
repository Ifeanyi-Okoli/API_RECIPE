from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=250)
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return self.title
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name