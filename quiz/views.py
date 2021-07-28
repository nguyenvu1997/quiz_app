from django.http import request, JsonResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Question, Quiz
from django.urls import reverse_lazy

class QuizTemplateView(TemplateView):
    template_name = 'quiz.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.all()
        return context

def QuizResult(request):
    # Get true answer from db
    results = request.GET

    questions = Question.objects.filter(question_text__in = list(results)[1:])
    dict_true_answer = {}
    for question in questions:
        q = (question.question_text)
        a = (question.get_true_answer()[0])
        dict_true_answer[q] = str(a)

    contents = []
    dict_answered = {}
    for result in list(results)[1:]:
        dict_answered['question'] = result
        dict_answered['answered'] = request.GET[result]
        dict_answered['true_answer'] = dict_true_answer[result]
        contents.append(dict_answered.copy())

    return render(request, 'quiz_result.html', {'contents' : contents})

class QuizList(ListView):
    model = Quiz
    template_name = 'quiz_list.html'
    context_object_name = 'quizs'

class QuizDetail(DetailView):
    model = Quiz
    template_name = 'quiz_detail.html'
    context_object_name = 'quiz'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choice'] = ['A', 'B', 'C', 'D']
        return context