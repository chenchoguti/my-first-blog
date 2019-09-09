from django import forms

from .models import Publicacion

class FormPub(forms.ModelForm):
	"""docstring for FormPub"""
	class Meta:
		model = Publicacion
		fields = ('titulo','texto',)
		