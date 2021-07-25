from django.http import request
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, FormView
from .models import Question, Quiz


# Create your views here.
# def quiz(request):
#     return render(request, 'quiz.html')

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


    def get_context_data(self, **kwargs):
        print(self.request)
        context = super().get_context_data(**kwargs)
        context['quizs'] = context['quizs'].all()

        search_input = self.request.GET.get('search-area') or ''
        select_input = self.request.GET.get('select-categories') or ''
        print(select_input)
        if select_input:
            context['quizs'] = context['quizs'].filter(category__startswith=select_input)

        context['search_input'] = search_input
        context['select_input'] = select_input

        return context

class QuizDetail(DetailView):
    model = Quiz
    template_name = 'quiz_detail.html'
    context_object_name = 'quiz'