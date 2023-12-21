from django.shortcuts import render
from django.views.generic import View
from .models import Project

# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
            projects = Project.objects.all()
            context = {
                  'projects': projects
            }
            return render(request, 'home.html', context)
