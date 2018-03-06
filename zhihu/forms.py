from django import forms
from .models import Answer, Issue


class AnswerForm(forms.Form):
    content = forms.CharField(strip=False)
    anonymity = forms.BooleanField(required=False)


class IssueForm(forms.Form):
    title = forms.CharField(max_length=128)
    description = forms.CharField(required=True)
    anonymity = forms.BooleanField(required=False)
