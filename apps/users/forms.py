from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from .models import User


def create_form_field(field_type, placeholder, css_class, required=True):
    return field_type(
        widget=forms.TextInput(
            attrs={
                "placeholder": placeholder,
                "class": css_class,
                "required": required,
            }
        )
    )


class RegistrationForm(UserCreationForm):
    first_name = create_form_field(forms.CharField, "Имя...", "inpPass")
    last_name = create_form_field(forms.CharField, "Фамилия...", "inpPass")
    username = create_form_field(forms.CharField, "Логин...", "inp90")
    email = create_form_field(forms.EmailField, "Почта...", "inp90")
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Пароль...", "class": "inpPass"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Повторите Пароль...", "class": "inpPass"}
        )
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )


class LoginForm(AuthenticationForm):
    username = create_form_field(forms.CharField, "Логин...", "inp90")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Пароль...", "class": "inp90"})
    )

    class Meta:
        model = User
        fields = ("username", "password")


class UserProfileForm(UserChangeForm):
    username = create_form_field(forms.CharField, "", "")
    first_name = create_form_field(forms.CharField, "", "")
    last_name = create_form_field(forms.CharField, "", "")
    email = create_form_field(forms.EmailField, "", "")
    image = forms.ImageField(widget=forms.FileInput(attrs={}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "image")
