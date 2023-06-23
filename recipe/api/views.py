from django.shortcuts import render
from rest_framework import generics
from .models import Recipe, Ingredient, Tag
from .serializers import RecipeSerializer, IngredientSerializer, TagSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.

class RecipeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()  # Retrieve all Recipe instances from the database
    serializer_class = RecipeSerializer  # Use the RecipeSerializer to serialize/deserialize Recipe instances

class RecipeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()  # Retrieve all Recipe instances from the database
    serializer_class = RecipeSerializer  # Use the RecipeSerializer to serialize/deserialize Recipe instances
    
class IngredientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()  # Retrieve all Ingredient instances from the database
    serializer_class = IngredientSerializer  # Use the IngredientSerializer to serialize/deserialize Ingredient instances
    
class IngredientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()  # Retrieve all Ingredient instances from the database
    serializer_class = IngredientSerializer  # Use the IngredientSerializer to serialize/deserialize Ingredient instances

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()  # Retrieve all Tag instances from the database
    serializer_class = TagSerializer  # Use the TagSerializer to serialize/deserialize Tag instances

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()  # Retrieve all Recipe instances from the database
    serializer_class = RecipeSerializer  # Use the RecipeSerializer to serialize/deserialize Recipe instances

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()  # Retrieve all Ingredient instances from the database
    serializer_class = IngredientSerializer  # Use the IngredientSerializer to serialize/deserialize Ingredient instances
