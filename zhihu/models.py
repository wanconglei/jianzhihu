from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Issue(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='issue')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    topic = models.ForeignKey(Topic, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    anonymity = models.BooleanField(default=False)

    class Meta:
        ordering = ['-create_time', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('zhihu:detail', kwargs={'pk': self.pk})


class Answer(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='answer')
    issue = models.ForeignKey(Issue, related_name='answer')
    content = models.TextField(default="")
    create_time = models.DateTimeField(auto_now_add=True)
    read_time = models.IntegerField(default=0)
    Status = (
        (0, '草稿'),
        (1, '已发布')
    )
    status = models.IntegerField(choices=Status, default=0)
    useless = models.BooleanField(default=False)
    agree = models.IntegerField(default=0)
    disagree = models.IntegerField(default=0)
    anonymity = models.BooleanField(default=False)

    class Meta:
        ordering = ['-create_time', '-read_time']


def __str__(self):
    return self.content[:17]


class Attitude(models.Model):
    Attitudes = (
        (-1, '反对'),
        (0, '未表态'),
        (1, '赞同'),
    )
    attitude = models.IntegerField(choices=Attitudes, default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_attitude')
    answer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='answer_attitude')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.attitude
