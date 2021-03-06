from django.urls import path

from .views import (
    about_page,
    RecipeListView,
    UserRecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView,
)


urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes-home"),
    path("about/", about_page, name="recipes-about"),
    path("user/<str:username>", UserRecipeListView.as_view(), name="user-recipes"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
    path("recipe/create/", RecipeCreateView.as_view(), name="recipe-create"),
    path("recipe/<int:pk>/update/", RecipeUpdateView.as_view(), name="recipe-update"),
    path("recipe/<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe-delete"),
]
