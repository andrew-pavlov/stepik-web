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

  def clean(self):
    return self.cleaned_data

  def save(self):
    answer = Answer(**self.cleaned_data)
    answer.author_id = 1
    answer.save()
    return answer

class SignupForm(forms.Form):
  username = forms.CharField()
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)

  def clean(self):
    return self.cleaned_data

  def save(self):
    user = User(**self.cleaned_data)
    user.save()
    return user
