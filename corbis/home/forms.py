from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto

class CustomUserCreationForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ProductoCreationForm(forms.ModelForm):
	
	class Meta:
		model = Producto
		#fields = '__all__'
		fields = ['codigo', 'nombre', 'tipo_id', 'precio', 'cantidad']
