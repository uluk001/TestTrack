from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from loguru import logger

from .forms import LoginForm, RegistrationForm


def authentication_view(request):
    form = LoginForm(data=request.POST) if request.method == "POST" else LoginForm()
    logger.info("Accessing authentication_view")

    if request.method == "POST" and form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            messages.success(request, f"{username}, вы успешно прошли авторизацию.")
            logger.info(f"User {username} authenticated successfully")
            return HttpResponseRedirect("/")
        else:
            messages.error(request, "Invalid username or password.")
            logger.warning(f"Authentication failed for user {username}")
    else:
        if request.method == "POST":
            messages.error(request, "Form is not valid. Please correct the errors.")
            logger.error("Form validation failed")

    context = {"form": form}
    return render(request, "users/login.html", context)


def registration_view(request):
    logger.info("Accessing registration_view")

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info(f"New user registered: {form.cleaned_data['username']}")
            messages.success(request, "Registration successful. Please log in.")
            return redirect("login")
        else:
            logger.error(f"Registration error: {form.errors}")
            messages.error(request, "Registration failed. Please correct the errors.")
            messages.error(request, form.errors)
    else:
        form = RegistrationForm()

    context = {
        "form": form,
        "login_form": LoginForm(),
        "registration_form": RegistrationForm(),
        "registration": True,
    }

    return render(request, "users/register.html", context)


def logout(request) -> HttpResponseRedirect:
    auth.logout(request)
    return HttpResponseRedirect("/")
