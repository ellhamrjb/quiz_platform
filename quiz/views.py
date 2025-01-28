from django.shortcuts import render
import random
from .models import Question
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import UserScore


def home(request):
    return render(request, 'quiz/home.html')

def start_quiz(request):
    questions = list(Question.objects.all())
    random.shuffle(questions)
    return render(request, 'quiz/quiz.html', {'questions': questions[:10]})


@login_required
def start_quiz(request):
    if request.method == 'POST':
        score = 0
        questions = Question.objects.all()
        for i, question in enumerate(questions[:10], start=1):
            user_answer = request.POST.get(f'q{i}')
            if user_answer and user_answer.lower() == question.correct_answer.lower():
                score += 1
        user_score, created = UserScore.objects.get_or_create(user=request.user)
        user_score.score += score
        user_score.save()
        return redirect('view_score')
    else:
        questions = list(Question.objects.all())
        random.shuffle(questions)
        return render(request, 'quiz/quiz.html', {'questions': questions[:10]})
    
@login_required
def view_score(request):
    user_score = UserScore.objects.get(user=request.user)
    return render(request, 'quiz/score.html', {'score': user_score.score})
