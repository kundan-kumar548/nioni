from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import *


class Signup(forms.Form):
    user_name = forms.CharField(label='Enter Username', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'username'}), min_length=6, max_length=150, required=True)
    email = forms.EmailField(label='Enter email', widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'email'}), required=True, max_length=50)
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'password'}), required=True)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'confirm password'}), required=True)

    def clean_username(self):
        username = self.cleaned_data["user_name"]
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data["user_name"],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        return user