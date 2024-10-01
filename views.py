from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import \
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
    
from .models import Report, Subject
from .forms import ReportForm, SubjectForm
from .myplot import line_charts, bar



class DashBoardView(TemplateView):
    """
    ダッシュボード画面を生成する
    """
    template_name = "study_report_support/dashboard.html"
    model = Report

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['subject_list'] = Subject.objects.all
        context["plot"] = bar(7)
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
    success_url = reverse_lazy('srs:index')

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
    success_url = reverse_lazy('srs:index')

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
    success_url = reverse_lazy('srs:index')

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
    success_url = reverse_lazy('srs:index')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object)
        )
        return result
