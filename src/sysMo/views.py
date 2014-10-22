from __future__ import unicode_literals 
from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required


def home(request):
    if (request.user.is_authenticated()):
        return render(request, 'home.html')
    return login(request, template_name='home.html')

def sampleReport1(request):
    if (request.user.is_authenticated()):
        return render(request, 'sampleReport1.html')
    return login(request, template_name='sampleReport1.html')

def sampleReport2(request):
    if (request.user.is_authenticated()):
        return render(request, 'sampleReport2.html')
    return login(request, template_name='sampleReport2.html')  

def sampleReport3(request):
    if (request.user.is_authenticated()):
        return render(request, 'sampleReport3.html')
    return login(request, template_name='sampleReport3.html')        

def aboutus(request):
    if (request.user.is_authenticated()):
        return render(request, 'aboutus.html')
    return login(request, template_name='aboutus.html')

def contact(request):
    if (request.user.is_authenticated()):
        return render(request, 'contact.html')
    return login(request, template_name='contact.html')

@login_required
def profile(request):
    return render(request, template_name='profile.html')

@login_required
def platform(request):
    return render(request, template_name='platform.html')
