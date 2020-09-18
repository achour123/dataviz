from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class Participants (models.Model):
    
    LOCALISATION_CHOICES= [
        ('Tunis', 'Tunis'),
        ('Ariana', 'Ariana'),
        ('Ben Arous', 'Ben Arous'),
        ('Manouba', 'Manouba'),
        ('Nabeul', 'Nabeul'),
        ('Bizert', 'Bizert'),
        ('Zaghouan', 'Zaghouan'),
        ('Sousse', 'Sousse'),
        ('Monastir', 'Monastir'),
        ('Mahdia', 'Mahdia'),
        ('Sfax', 'Sfax'),
        ('Beja', 'Beja'),
        ('Jendouba', 'Jendouba'),
        ('El_kef', 'El kef'),
        ('Seliana', 'Seliana'),
        ('Kairouane', 'Kairouane'),
        ('Sidi_Bouzid', 'Sidi Bouzid'),
        ('Kasserine', 'Kasserine'),
        ('Gabes', 'Gabes'),
        ('Medenine', 'Medenine'),
        ('Gafsa', 'Gafsa'),
        ('Tozeur', 'Tozeur'),
        ('Tataouine', 'Tataouine'),
        ('kébili', 'kébili'),
    ]

    CIVIL_CHOICES= [
       ('Seul(e)','Seul(e)'),
       ('Marié(e)','Marié(e)'),
       ('Colocation','Colocation'),
       ('Avec Enfant(s)','Avec Enfant(s)'),
       ('Personne(s) agée(s) à charge','Personne(s) agée(s) à charge'),
    ]

    SYMPTOMES_CHOICES= [
        ('fievre','fiévre(temperature>37.8°C)'),
        ('respiratoire','toux ou difficulté respiratoire'),
        ('diarrhe','diarrhée (au moins 3selles molles/j)'),
        ('cephalees','céphalées (maux de tête)'),
        ('douleurs','douleurs musculaires et courbatures'),
        ('odorat','perte de l\'odorat'),
        ('appetit','perte de l\'appétit'),
        ('fatigue','fatigue inhabituelle'),
        ('sympt','Pas de symptômes'),
    ]

    ANTECEDENTS_CHOICES=[
        ('hypertension','hypertension mal équilibrée'),
        ('diabete','diabète'),
        ('maladieRespiratoire','maladie respiratoire'),
        ('renale','insuffisance rénale'),
        ('immunitaire','insuffisance immunitaire'),
        ('fumeur','fumeur'),
        ('rien','Pas d\'antécédents'),
    ]

    ETRANGER_CHOICES= [
        ('oui','oui'),
        ('non','non'),
    ]

    VOYAGE_CHOICES= [
        ('oui','oui'),
        ('non','non'),
    ]

    CONTACT_CHOICES= [
        ('oui','oui'),
        ('non','non'),
    ]

    nom= models.CharField(max_length=20)
    prenom= models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    localisation = models.CharField(max_length=30, choices=LOCALISATION_CHOICES)
    civil=models.CharField(max_length=120, choices=CIVIL_CHOICES)
    symptomes=MultiSelectField(choices=SYMPTOMES_CHOICES)
    antecedents=MultiSelectField(choices=ANTECEDENTS_CHOICES)
    etranger=models.CharField(max_length=3,choices=ETRANGER_CHOICES)
    voyage=models.CharField(max_length=3,choices=VOYAGE_CHOICES)
    contact=models.CharField(max_length=3,choices=CONTACT_CHOICES)

    def __str__(self):
        return self.nom
    
    
