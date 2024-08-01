from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main_page(request):
    return HttpResponse("Hello, world. You're at the study_report_support main page.")