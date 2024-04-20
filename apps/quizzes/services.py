from .models import Quiz, Question
from django.shortcuts import get_object_or_404


class QuizService:

    def get_all_quizzes(self):
        return Quiz.objects.all()

    def get_quiz(self, quiz_id):
        return get_object_or_404(Quiz, id=quiz_id)

    def get_quiz_with_questions(self, quiz_id):
        quiz = get_object_or_404(Quiz, id=quiz_id)
        questions = quiz.questions.all()
        return quiz, questions


class QuestionService:

    def get_questions(self, quiz_id):
        return Question.objects.filter(quiz_id=quiz_id)

    def get_question(self, question_id):
        return Question.objects.get(id=question_id)

    def get_question_with_choices(self, question_id):
        question = get_object_or_404(Question, id=question_id)
        choices = question.choices.all()
        return question, choices
