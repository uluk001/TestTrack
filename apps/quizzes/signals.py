from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from apps.quizzes.models import Question


# @receiver(post_save, sender=Question)
# def validate_question_choices(sender, instance, **kwargs):

#     if not instance.choices.filter(is_correct=True).exists():
#         raise ValidationError("At least one correct answer is required.")

#     if instance.choices.count() == instance.choices.filter(is_correct=True).count():
#         raise ValidationError("Not all answers can be correct.")
