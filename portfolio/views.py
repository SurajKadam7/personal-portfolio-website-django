from django.shortcuts import render

# to featch data from the database we use below command and django made it easy for us if we don't use dango then we need to manually featch all data using sql and then send back in python objcet all this is avoided by django
from .models import Project

def home(request):
    # in projects_data we are collecting all the info in stored in database.
    projects_data = Project.objects.all()

    return render(request, 'portfolio/home.html', {'projects_data' : projects_data})

# Create your views here.
