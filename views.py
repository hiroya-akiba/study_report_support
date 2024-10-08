from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import \
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
import json

from .models import Report, Subject
from .forms import ReportForm, SubjectForm
from .myplot import UsePlotly, UseMatplotlib

import plotly.graph_objects as go
from plotly.utils import PlotlyJSONEncoder

class DashBoardView(TemplateView):
    """
    ダッシュボード画面を生成する
    """
    template_name = "study_report_support/dashboard.html"
    model = Report
    plot_obj = UsePlotly
    #plot_obj = UseMatplotlib()
    #plot_obj.create_graph()

    def post(self, request):
        data = json.loads(request.body)
        print(f"Received data: {data}")
        return JsonResponse({'status': 'success'})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['subject_list'] = Subject.objects.all
        context["plot"] = self.plot_obj.bar(7)
        #context["plot"] = self.plot_obj.get_image()
        return context


class ReportListview(ListView):
    """
    レポートを一覧表示する
    テンプレートは指定しない場合、モデル名_list.htmlが使われる
    """
    template_name = "study_report_support/index.html"
    model = Report
    paginate_by = 10
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['subject_list'] = Subject.objects.all
        return context



class ReportDetailView(DetailView):
    """
    レポートを詳細表示する
    モデル名_detail.htmlが使用される
    """
    template_name = "study_report_support/detailReport.html"
    model = Report



class ReportCreateView(CreateView):
    """
    レポートを新規作成する
    django.contriv.messagesを使用するとPRGが使える
    """
    template_name = "study_report_support/createReport.html"
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('srs:dash_board')

    def from_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を作成しました'.format(form.instance)
        )
        return result



class SubjectCreateView(CreateView):
    """
    科目を新規作成する
    """
    template_name = "study_report_support/createSubject.html"
    model = Subject
    form_class = SubjectForm
    success_url = reverse_lazy('srs:dash_board')

    def from_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を作成しました'.format(form.instance)
        )
        return result



class ReportUpdateview(UpdateView):
    """
    レポートを編集する
    """
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('srs:dash_board')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を更新しました'.format(form.instance)
        )
        return result
    


class ReportDeleteView(DeleteView):
    """
    レポートを削除する
    論理削除する場合は、deleteをオーバーライドする
    """
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('srs:dash_board')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object)
        )
        return result


class PlotlyExperimentView(ListView):
    """
    Plotlyの実験用ページ
    """
    template_name = "study_report_support/plotlyExperiment.html"
    regions = ['North', 'South', 'East', 'West']
    values = [20, 30, 15, 35]
    model = Report
    fig = go.Figure()
    for region, value in zip(regions, values):
        fig.add_trace(go.Bar(
            y=['Total'],
            x=[value],
            name=region,
            orientation='h',
            hovertemplate=f"Region: {region}<br>Value: %{{x}}<extra></extra>"
        ))
    fig.update_layout(barmode='stack')
    plot_json = json.dumps(fig, cls=PlotlyJSONEncoder)

    def post(self, request):
        data = json.loads(request.body)
        print(f"Received data: {data}")
        return JsonResponse({'status': 'success'})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['plot_json'] = self.plot_json
        return context
    
