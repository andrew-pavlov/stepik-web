from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm

def test(request, *args, **kwargs):
  return HttpResponse('OK')

def new(request):
  questions = Question.objects.new()
  page = request.GET.get('page', 1)
  paginator = Paginator(questions, 10)
  paginator.baseurl = '/?page='
  page = paginator.page(page)
  return render(request, 'new.html', {
    'questions': page.object_list,
    'paginator': paginator,
    'page': page,
  })

def popular(request):
  questions = Question.objects.popular()
  page = request.GET.get('page', 1)
  paginator = Paginator(questions, 10)
  paginator.baseurl = '/popular?page='
  page = paginator.page(page)
  return render(request, 'popular.html', {
    'questions': page.object_list,
    'paginator': paginator,
    'page': page,
  })

def question(request, id):
  question = get_object_or_404(Question, id=id)
  answers = question.answer_set.all()
  if request.method == 'POST':
    form = AnswerForm(request.POST)
    if form.is_valid():
      answer = form.save(request.user)
      url = question.get_url()
      return HttpResposeRedirect(url)
  else:
    form = AnswerForm()
  
  return render(request, 'question.html', {
    'question': question,
    'answers': answers,
    'form': form,
  })

def ask(request):
  if request.method == 'POST':
    form = AskForm(request.POST)
    if form.is_valid():
      question = form.save(request.user)
      url = question.get_url()
      return HttpResponseRedirect(url)
  else:
    form = AskForm()
  return render(request, 'ask.html', {
    'form': form,
  })
  
def signup(request):  
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save()
      user = authenticate(**form.cleaned_data)
      if user:
        login(request, user)
        return HttpResponseRedirect('/')
  else:
    form = SignupForm()
  return render(request, 'signup.html', {
    'form': form,
  })

def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      user = authenticate(**form.cleaned_data)
      if user:
        login(request, user)
        return HttpResponseRedirect('/')
  else:
    form = LoginForm()
  return render(request, 'login.html', {
    'form': form,
  })
