from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')

def projects(request):
    return render(request, 'projects.html')

from .models import Contact
from django.http import HttpResponse
def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.phone=phone
        contact.message=message
        contact.save()
        return HttpResponse("<h1>Thank You for contact us</h1>")
        
    return render(request, 'contact.html')