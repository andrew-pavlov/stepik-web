from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateField()
  rating = models.IntegerField()
  author = models.ForeignKey(User)
  likes = models.ManyToManyField(User, related_name='likes_set')

class QuestionManager(models.Manager):
  def new(self):
    return Question.objects.all().order_by('-added_at')
  def popular(self):
    return Question.objects.all().order_by('-rating')
    

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateField()
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User)
