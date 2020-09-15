from django import forms
from .models import Participants

class ParticipantsForm(forms.ModelForm):
    class Meta:
        model = Participants 
        fields = ['nom','prenom', 'email', 'localisation','civil','symptomes','antecedents','etranger','voyage','contact']
        
        
        widgets = {
            'nom' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Votre Nom','required': True}),
            'prenom' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Votre Prenom','required': True}),
            'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'vous@email.com' ,'required': True}),
            'localisation' : forms.Select(attrs={'class': 'form-control','required': True}),
            'civil' : forms.Select(attrs={'class': 'form-control','required': True}),
            'etranger': forms.Select(attrs={'class': 'form-control','required': True}),
            'voyage' : forms.Select(attrs={'class': 'form-control','required': True}),
            'contact' : forms.Select(attrs={'class': 'form-control','required': True}),

        }
        