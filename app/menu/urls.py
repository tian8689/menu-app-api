from django.urls import path, include
from rest_framework.routers import DefaultRouter

from menu import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'menu'

urlpatterns = [
    path('', include(router.urls))
]