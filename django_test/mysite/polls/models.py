# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
        
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

class TestCase(models.Model):
    name = models.TextField(max_length=100)
    tester = models.TextField(max_length=50)
    status_choices = (
        ('NR', "Not Run"),
        ('PA', "PASS"),
        ('FA', "FAIL"),
        ('BL', "BLOCKED"),
        ('NI', "Not Implemented")
    )
    status = models.CharField(
        max_length=2,
        choices=status_choices,
        default='NR',
    )
    comment = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class TestPlan(models.Model):
    name = models.TextField(max_length=100)
    tests = []

    def __str__(self):
        return self.name

    def add_test(self, test):
        self.tests.append(test)

    def remove_test(self, test):
        self.tests.remove(test)
