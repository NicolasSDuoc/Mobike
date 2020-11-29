from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms import widgets
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label = 'Confirme su contraseña', widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Confirme su contraseña',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','phone','commune']
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su rut',
                    'id': 'username',
                    'required': 'required',
                }
            ),
            'first_name': forms.TextInput( 
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'id': 'first_name',
                    'required': 'required',
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido',
                    'id': 'last_name',
                    'required': 'required',
                }
            ),
            'email': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo',
                    'id': 'email',
                    'required': 'required',
                }
            ),
            'phone': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su teléfono',
                    'id': 'phone',
                    'required': 'required',
                }
            ),
            'commune': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'id': 'commune',
                    'required': 'required',
                }
            ),
        }
    class media:
        js = ('./static/app/custom.js')