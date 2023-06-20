from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from api import views
from api.views import RecipeViewSet, IngredientViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
