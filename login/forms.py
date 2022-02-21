from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Student


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'mobile_number', 'name_first')


# class StudentCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = Student
#         fields = ('name', 'age', 'id')
