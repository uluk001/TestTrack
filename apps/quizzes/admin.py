from typing import Any
from django.contrib import admin

from apps.quizzes.forms import ChoiceInlineFormset
from .models import Quiz, Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    formset = ChoiceInlineFormset
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

    def get_formsets_with_inlines(self, request: Any, obj: Any = None) -> Any:
        for inline in self.get_inline_instances(request, obj):
            yield inline.get_formset(request, obj), inline


class QuizAdmin(admin.ModelAdmin):
    pass


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
