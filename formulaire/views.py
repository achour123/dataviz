from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ParticipantsForm
import csv

# Create your views here.
def formul(request):
    if request.method=='POST':
        form = ParticipantsForm(request.POST)
        if form.is_valid():
            form.save()
            with open("./consult.csv", 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=form.cleaned_data.keys())
                writer.writerow(form.cleaned_data)
                return redirect("/")
        else:
            form = ParticipantsForm()

    form=ParticipantsForm()
    return render(request,'formulaire/formul.html',{'form' : form})
