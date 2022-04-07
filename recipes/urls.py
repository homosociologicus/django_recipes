from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="recipes-home"),
    path("about/", views.about_page, name="recipes-about"),
]
