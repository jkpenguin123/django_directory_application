from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.db import connection
from .models import *

from .forms import MyUserCreationForm


# Create your views here.

def index(request):
    return render(request=request, template_name="C:/Users/ajay7/projects/directory_application/templates/home.html")


def register(request):
    return render(request=request, template_name="home.html")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                # GET THE USER FROM OUR OWN DATABASE
            else:

                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="C:/Users/ajay7/projects/directory_application/templates/login.html", context={"login_form": form})

