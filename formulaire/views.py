from django.shortcuts import render

from .forms import ParticipantsForm

# Create your views here.
def formul(request):
    if request.method=='POST':
        form = ParticipantsForm(request.POST)
        if form.is_valid():            
            print("valid")
            form.save()
        else:
            form = ParticipantsForm()

    form=ParticipantsForm()
    return render(request,'formulaire/formul.html',{'form' : form})