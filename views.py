from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the study report support index.")

# Use Template
class Index(TemplateView):
    template_name = "index.html"