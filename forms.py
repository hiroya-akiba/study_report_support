from django.forms import ModelForm, Textarea
from .models import Report, Subject

class ReportForm(ModelForm):
    class Meta:
        model = Report
        # forms.Formの記載方法
        #subject = forms.CharField()
        #time = forms.IntegerField()

        # forms.ModelFormの記載方法
        # fields: fieldsで指定したフィールドが入力フォームとして表示される
        fields = ('subject', 'time', )
        labels = {
            'subject':'科目',
            'time':'時間',
        }

        #widgets = {
        #    "subject": Textarea(attrs={'cols':30, 'rows':1})
        #}

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        # fields: fieldsで指定したフィールドが入力フォームとして表示される
        fields = ('subject_name', )
        labels = {
            'subject_name':'科目名'
        }
