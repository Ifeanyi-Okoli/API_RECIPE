from django.db import models
from django.core.validators import FileExtensionValidator
from django_resized import ResizedImageField

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()
    image = ResizedImageField(upload_to='recipe_images', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], size=[500, 500], quality=75, blank=True, null=True)

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