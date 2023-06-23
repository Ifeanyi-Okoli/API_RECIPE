from django.db import models
from django.core.validators import FileExtensionValidator
from django_resized import ResizedImageField

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)  # Field to store the title of the recipe
    ingredients = models.TextField()  # Field to store the list of ingredients as text
    time_required = models.CharField(max_length=50)  # Field to store the time required to prepare the recipe
    instructions = models.TextField()  # Field to store the cooking instructions as text
    image = ResizedImageField(
        upload_to='recipe_images',  # Directory to upload the recipe image
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],  # Validators to restrict the file extension
        size=[500, 500],  # Size to resize the uploaded image
        quality=75,  # Image quality after resizing
        blank=True,  # The image field is not required
        null=True  # The image field can be null
    )

    def __str__(self):
        return self.title  # String representation of the Recipe instance

class Ingredient(models.Model):
    name = models.CharField(max_length=100)  # Field to store the name of the ingredient
    description = models.TextField()  # Field to store the description of the ingredient
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)  # Foreign key relationship to associate an ingredient with a recipe
    quantity = models.CharField(max_length=50)  # Field to store the quantity of the ingredient needed for the recipe
    
    def __str__(self):
        return self.name  # String representation of the Ingredient instance

class Tag(models.Model):
    name = models.CharField(max_length=100)  # Field to store the name of the tag
    description = models.TextField()  # Field to store the description of the tag
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)  # Foreign key relationship to associate a tag with a recipe

    def __str__(self):
        return self.name  # String representation of the Tag instance
