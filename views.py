from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views.generic import TemplateView
from .models import Report, Subject
from .forms import ReportForm, SubjectForm


class SrsIndexView(TemplateView):
    template_name = './study_report_support/index.html'

    # *argsはタプル型で、**kwargsは辞書型で引数を受け取る
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs): # request変数が引数に入っていないので、使えないように思えるが、
        # viewのインスタンス変数についているので、問題なく使うことができる。
        latest_report_list = Report.objects.order_by('create_time')[:5]
        context = super().get_context_data(**kwargs) # 親のcontext_dataをインスタンス化する。
        context['latest_report_list'] = latest_report_list # 独自のコンテキスト情報を設定する。
        return context # DB情報を取得するなどの動的なコンテキストを設定する場合は、このように継承して使用する。

index = SrsIndexView.as_view()


#def index(request):
#    # create_dateカラムから5行分
#    latest_report_list = Report.objects.order_by('create_time')[:5]
#    #for in で1行ずつ latestreport を出力して , で繋げる
#    # output = ','.join([rep.subject for rep in latest_report_list])
#    # return HttpResponse(output)
#    template = loader.get_template('study_report_support/index.html')
#    context = {
#        'latest_report_list' : latest_report_list,
#    }
#    return HttpResponse(template.render(context, request))

def create(request):
    if request.method == 'POST':
        rf = ReportForm(request.POST)
        if rf.is_valid():
            rf.save()
        context = {}
        url = 'study_report_support/index.html'
    else :
        if 'create_report' in request.path_info :
            rf = ReportForm()
            url = 'study_report_support/createReport.html'
            context = {
                'reportForm' : rf,
            }
        elif 'create_subject' in request.path_info :
            sf = SubjectForm()
            url = 'study_report_support/createSubject.html'
            context = {
                'subjectForm' : sf,
            }
    return render(request, url, context)
