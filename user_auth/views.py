import imp
from xml.etree.ElementTree import C14NWriterTarget
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"You have successfully registered as {username}",
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    context = {
        "form": form,
    }
    return render(
        request,
        "user_auth/register.html",
        context,
    )


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(
            data=request.POST,
            instance=request.user,
        )
        profile_form = ProfileUpdateForm(
            data=request.POST,
            files=request.FILES,
            instance=request.user.profile,
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request,
                "You have successfully updated your profile",
            )
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(
        request,
        "user_auth/profile.html",
        context,
    )
