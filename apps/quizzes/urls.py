from django.urls import path
from .views import (
    quizzes_view,
    quiz_view,
    start_quiz,
    take_question,
    quiz_results,
)

urlpatterns = [
    path("quizzes/", quizzes_view, name="quizzes"),
    path("quiz/<int:quiz_id>/", quiz_view, name="quiz"),
    path("quiz/<int:quiz_id>/start/", start_quiz, name="start_quiz"),
    path("question/<int:question_id>/", take_question, name="take_question"),
    path("results/<int:quiz_id>/", quiz_results, name="quiz_results"),
]
