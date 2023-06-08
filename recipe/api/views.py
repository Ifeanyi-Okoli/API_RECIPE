from django.shortcuts import render
from rest_framework import generics
from .models import Recipe, Ingredient, Tag
from .serializers import RecipeSerializer, IngredientSerializer, TagSerializer

# Create your views here.

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
