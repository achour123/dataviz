from django.shortcuts import render

def home(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')

def handler404(request):
    return render(request,'errors/404.html',{},status=404)    
        


    