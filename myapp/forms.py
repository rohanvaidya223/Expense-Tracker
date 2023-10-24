from django import forms
from django.forms import ModelForm
from .models import Expense
from django.contrib.auth.models import User


class ExpenseForm(ModelForm):
    
    class Meta:
        model = Expense
        fields = {'name','amount','category'}

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {'username','email','first_name','last_name'}

        def check_password(self):
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError('Password Do not Match')
            
            return self.cleaned_data['password2']
                