from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("projects", views.projects, name="projects"),
    path("contact", views.contact, name="contact"),
    path("resume", views.resume, name="resume")
    ]

urlpatterns += staticfiles_urlpatterns()
