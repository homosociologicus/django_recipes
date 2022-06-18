from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Recipe


def about_page(request):
    context = {
        "title": "About Recipes Project",
    }
    return render(
        request,
        "recipes/about.html",
        context,
    )


class RecipeListView(ListView):
    model = Recipe

    # usually looks in "{app}/{model}_{view_type}.html"
    template_name = "recipes/home.html"
    context_object_name = "recipes"
    ordering = [
        "-datetime_posted",
    ]


class RecipeDetailView(DetailView):
    model = Recipe


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = [
        "title",
        "content",
    ]

    # override to fill "author" field in db
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = [
        "title",
        "content",
    ]

    # override to fill "author" field in db
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # check that user that updates a recipe is its author
    def test_func(self):
        return self.request.user == self.get_object().author


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = "/"

    # check that user that deletes a recipe is its author
    def test_func(self):
        return self.request.user == self.get_object().author
