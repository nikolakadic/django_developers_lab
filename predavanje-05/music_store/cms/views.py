from django.shortcuts import render
from .models import Service


def pricing(request):
    services = Service.objects.all()
    return render(request, 'cms/pricing.html', {'services':services})

def homepage(request):
    return render(request, 'cms/homepage.html', {})
