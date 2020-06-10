from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password','id':'login-password'}),)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password','id':'login-password'}),)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Username',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'First name',
                # 'autofocus': True,
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Last name',
            }),
        }
        help_texts = {
            'username': None,
        }



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder': 'Password',
    }))
    class Meta:
        model = User
        fields = ['username', 'password']