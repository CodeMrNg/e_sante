from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm , TextInput
from django import forms
from .models import AllUser, Consultation 


class AllUserCreationForm(UserCreationForm):
    class Meta:
        model = AllUser
        fields = ('name','firstname','genre','email','langue','status','specialite','password1', 'password2' )



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')


class ConsultationForm(ModelForm):
    class Meta:
        model = Consultation
        fields = ('medecin','patient','interprete' )