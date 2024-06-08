# forms.py  ity le code nopieko
from django import forms
from .models import VotreModele

class VotreModeleForm(forms.ModelForm):
    class Meta:
        model = VotreModele
        fields = ['champ1', 'champ2']  # Ajoutez d'autres champs selon vos besoins
