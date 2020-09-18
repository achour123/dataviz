from django.shortcuts import render
from django.http import HttpResponse
from .forms import ParticipantsForm

# Create your views here.
def formul(request):
    if request.method=='POST':
        form = ParticipantsForm(request.POST)
        if form.is_valid():  
            nom= form.cleaned_data['nom']          
            prenom= form.cleaned_data['prenom']          
            email= form.cleaned_data['email']       
            print("valid")
            form.save()
        else:
            form = ParticipantsForm()

    form=ParticipantsForm()
    return render(request,'formulaire/formul.html',{'form' : form})