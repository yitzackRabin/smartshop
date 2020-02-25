from django import forms

from userauth.models import Login


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'email', 'password', 'confirm_password']

