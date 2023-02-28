from django import forms

class LoginForm(forms.Form):
    
    userName = forms.CharField()
    passWord = forms.CharField(widget=forms.PasswordInput)