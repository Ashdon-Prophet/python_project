from .models import User
from django import forms
from django.forms import ModelForm, PasswordInput

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {'password': PasswordInput(), 'confirm_password': PasswordInput()}

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {'password': PasswordInput}
