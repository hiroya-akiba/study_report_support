from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import \
    ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Report
from .forms import ReportForm

class ReportListview(ListView):
    """
    レポートを一覧表示する
    テンプレートは指定しない場合、モデル名_list.htmlが使われる
    """
    template_name = "study_report_support/index.html"
    model = Report
    paginate_by = 10


class ReportDetailView(DetailView):
    """
    レポートを詳細表示する
    モデル名_detail.htmlが使用される
    """
    model = Report


class ReportCreateView(CreateView):
    """
    レポートを新規作成する
    django.contriv.messagesを使用するとPRGが使える
    """
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy('srs:index')

    def from_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を作成しました'.format(form.instance)
        )
        return result