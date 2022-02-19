from django.shortcuts import render
from matplotlib.style import context
# from django.http import HttpResponse
from .models import Recipe


def home_page(request):
    context = {
        'recipes': Recipe.objects.all(),
    }
    # return HttpResponse('<h1>Recipes Home</h1>')
    return render(
        request,
        'recipes/home_page.html',
        context,
    )


def about_page(request):
    context = {
        'title': 'About Recipes Project',
    }
    # return HttpResponse('<h1>About Recipes Project</h1>')
    return render(
        request,
        'recipes/about_page.html',
        context,
    )
