from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm

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
      answer = form.save()
      url = question.get_url()
      return HttpResposeRedirect(url)
  else:
    form = AnswerForm()
  
  return render(request, 'question.html', {
    'question': question,
    'answers': answers,
    'form': form
  })

def ask(request):
  if request.method == 'POST':
    form = AskForm(request.POST)
    if form.is_valid():
      question = form.save()
      url = question.get_url()
      return HttpResponseRedirect(url)
  else:
    form = AskForm()
  return render(request, 'ask.html', {
    'form': form
  })
  
