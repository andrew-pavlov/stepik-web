from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import datetime

# Create your models here.

class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-id')
  def popular(self):
    return self.order_by('-rating')

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField(default='')
  added_at = models.DateField(default=datetime.date.today)
  rating = models.IntegerField(default=0)
  author = models.ForeignKey(User)
  likes = models.ManyToManyField(User, related_name='likes_set')
  objects = QuestionManager()

  def get_url(self):
    return reverse('question', kwargs={'id': self.id})

  def __unicode__(self):
    return self.title

class Answer(models.Model):
  text = models.TextField(default='')
  added_at = models.DateField(default=datetime.date.today)
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User)

  def __unicode__(self):
    return self.text
