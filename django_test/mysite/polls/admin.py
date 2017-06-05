# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Choice, Question, TestCase


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class TestCaseAdmin(admin.ModelAdmin):
    model = TestCase

admin.site.register(Question, QuestionAdmin)
admin.site.register(TestCase, TestCaseAdmin)
