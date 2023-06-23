from rest_framework import serializers
from .models import Recipe, Ingredient, Tag

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'description', 'recipe', 'quantity']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    # tags = TagSerializer(many=True)
    # ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_required', 'instructions', 'image']
        
    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])  # Extract tags data from validated_data (defaulting to an empty list if not present)
        ingredients_data = validated_data.pop('ingredients', [])  # Extract ingredients data from validated_data (defaulting to an empty list if not present)

        recipe = Recipe.objects.create(**validated_data)  # Create a new Recipe instance using the remaining validated_data

        for tag_data in tags_data:
            Tag.objects.create(recipe=recipe, **tag_data)  # Create a Tag instance and associate it with the recipe

        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient_data)  # Create an Ingredient instance and associate it with the recipe

        return recipe  # Return the created Recipe instance

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])  # Extract tags data from validated_data (defaulting to an empty list if not present)
        ingredients_data = validated_data.pop('ingredients', [])  # Extract ingredients data from validated_data (defaulting to an empty list if not present)

        instance.title = validated_data.get('title', instance.title)  # Update the title of the Recipe instance with the new value if provided
        instance.time_required = validated_data.get('time_required', instance.time_required)  # Update the time_required field if provided
        instance.instructions = validated_data.get('instructions', instance.instructions)  # Update the instructions field if provided
        instance.image = validated_data.get('image', instance.image)  # Update the image field if provided
        instance.save()  # Save the changes made to the Recipe instance

        instance.tags.all().delete()  # Remove all existing tags associated with the Recipe instance
        for tag_data in tags_data:
            Tag.objects.create(recipe=instance, **tag_data)  # Create a new Tag instance and associate it with the recipe

        instance.ingredients.all().delete()  # Remove all existing ingredients associated with the Recipe instance
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=instance, **ingredient_data)  # Create a new Ingredient instance and associate it with the recipe

        return instance  # Return the updated Recipe instance
