from __future__ import unicode_literals 
from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required

@login_required
def plots_home(request):
    return render(request, template_name='plots/plots_home.html')