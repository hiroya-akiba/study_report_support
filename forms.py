from django import forms

class ReportForm(forms.Form):
    subject = forms.CharField()
    time = forms.IntegerField()
