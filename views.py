from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views.generic import TemplateView
from .models import Report, Subject
from .forms import ReportForm

# Create your views here.
def index(request):
    # create_dateカラムから5行分
    latest_report_list = Report.objects.order_by('create_time')[:5]
    #for in で1行ずつ latestreport を出力して , で繋げる
    # output = ','.join([rep.subject for rep in latest_report_list])
    # return HttpResponse(output)
    template = loader.get_template('study_report_support/index.html')
    context = {
        'latest_report_list' : latest_report_list,
    }
    return HttpResponse(template.render(context, request))

def createReport(request):
    # POSTメソッドの場合
    if request.method == 'POST':
        rf = ReportForm(request.POST)
        if rf.is_valid():
            rf.save()
    # GETメソッドの場合
    else:
        rf = ReportForm()
        url = 'study_report_support/createReport.html'
    context = {
        'reportForm' : rf,
    }
    return render(request, url, context)