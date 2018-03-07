from django import forms
from qa.models import Question
from django.contrib.auth.models import User

class AskForm(forms.Form):
  title = forms.CharField()
  text = forms.CharField()

  def clean(self):
    return self.cleaned_data

  def save(self):
    question = Question(**self.cleaned_data)
    question.author_id = 1
    question.save()
    return question

class AnswerForm(forms.Form):
  text = forms.CharField()
  question = forms.IntegerField()
