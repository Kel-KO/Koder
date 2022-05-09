from this import d
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Koder/index.html")
def projects(request):
    return render(request, "Koder/projects.html") 
def contact(request):
    return render(request, "Koder/contact.html")
def resume(request):
    return render(request, "Koder/resume.html")