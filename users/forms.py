from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from users.models import CustomUser


class SignInForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

# class SignInForm(forms.ModelForm):
    # password = forms.CharField(label='Password', widget=forms.PasswordInput)
    #
    # class Meta:
    #     model = CustomUser
    #     fields = ['username', 'password']

    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get('username')
    #     password = cleaned_data.get('password')
    #
    #     user = authenticate(username=username, password=password)
    #     if not user:
    #         raise forms.ValidationError('Invalid username or password')
    #     return cleaned_data
