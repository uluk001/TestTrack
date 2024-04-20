from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from loguru import logger

from .services import QuestionService, QuizService


def main_view(request):
    quiz_service = QuizService()
    quizzes = quiz_service.get_all_quizzes()
    return render(request, "main.html", {"quizzes": quizzes})


def quizzes_view(request):
    quiz_service = QuizService()
    quizzes = quiz_service.get_all_quizzes()
    return render(request, "quizzes/quizzes.html", {"quizzes": quizzes})


def quiz_view(request, quiz_id):
    quiz_service = QuizService()
    quiz, questions = quiz_service.get_quiz_with_questions(quiz_id)
    logger.info(f"User {quiz.id} viewed quiz {quiz}")
    return render(request, "quizzes/quiz.html", {"quiz": quiz})


@login_required
def start_quiz(request, quiz_id):
    quiz_service = QuizService()
    quiz, questions = quiz_service.get_quiz_with_questions(quiz_id)

    request.session["quiz"] = {
        "id": quiz.id,
        "questions": [question.id for question in questions],
        "current_index": 0,
        "answers": {},
    }
    return redirect("take_question", question_id=questions[0].id)


@login_required
def take_question(request, question_id):
    quiz_session = request.session.get("quiz", None)

    logger.info(f"User {request.user.id} is taking question {question_id}")

    if quiz_session is None:
        logger.info(f"User {request.user.id} is starting a new quiz")
        return redirect("start_quiz", quiz_id=quiz_session["id"])

    current_index = quiz_session["current_index"]
    questions = quiz_session["questions"]

    if question_id != questions[current_index]:
        messages.error(request, "Please answer the current question before moving on.")
        question_id = questions[current_index]

    question_service = QuestionService()
    question, choices = question_service.get_question_with_choices(question_id)

    if request.method == "POST":
        selected_choice = request.POST.get("choice")

        if not selected_choice:
            messages.error(request, "You must select an answer.")
        else:
            quiz_session["answers"][str(question_id)] = selected_choice
            request.session.modified = True

            if current_index + 1 < len(questions):
                quiz_session["current_index"] += 1
                request.session.modified = True
                return redirect(
                    "take_question", question_id=questions[current_index + 1]
                )
            else:
                return redirect("quiz_results", quiz_id=quiz_session["id"])

    return render(
        request,
        "quizzes/take_question.html",
        {"question": question, "choices": choices},
    )


@login_required
def quiz_results(request, quiz_id):
    quiz_session = request.session.get("quiz", None)

    if quiz_session is None or str(quiz_id) != str(quiz_session["id"]):
        messages.error(request, "There was an error with your quiz session.")
        return redirect("quizzes")

    quiz_service = QuizService()
    quiz, questions = quiz_service.get_quiz_with_questions(quiz_id)

    correct_answers = 0

    for question_id, selected_choice in quiz_session["answers"].items():

        question = questions.get(id=int(question_id))
        if question.choices.get(id=int(selected_choice)).is_correct:
            correct_answers += 1

    total_questions = len(questions)
    score = correct_answers / total_questions * 100

    context = {
        "quiz": quiz,
        "correct_answers": correct_answers,
        "total_questions": total_questions,
        "score": score,
    }

    del request.session["quiz"]
    request.session.modified = True

    return render(request, "quizzes/quiz_results.html", context)
