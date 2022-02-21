from django.urls import path, include  # new
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.register, name="signup"),
    path("login/", views.login_request, name="login")

]

