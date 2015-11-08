from django import forms
from .models import Agendar
class PostForm(forms.ModelForm):
    class Meta:
        model = Agendar
        fields = ('actividad', 'descripcion','estado','fecha_actividad',)
