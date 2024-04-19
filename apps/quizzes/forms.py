from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError
from loguru import logger


class ChoiceInlineFormset(BaseInlineFormSet):

    def clean(self):
        super().clean()
        correct_answers = 0
        total_answers = 0

        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                total_answers += 1
                if form.cleaned_data.get('is_correct', False):
                    correct_answers += 1
                if form.cleaned_data.get('text', '').strip() == '':
                    raise ValidationError("Answer text is required.")

        logger.debug(f"Total answers: {total_answers}, correct answers: {correct_answers}")
        if correct_answers == 0:
            raise ValidationError("At least one correct answer is required.")
        if correct_answers == total_answers:
            raise ValidationError("Not all answers can be correct.")
