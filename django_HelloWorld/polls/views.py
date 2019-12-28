from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Question
def hello(request):
    return HttpResponse("hello world i'm studying django")
def index(request):
    question_list=Question.objects.all()
    count=len(question_list)
    context = {'question_list':question_list,'count':count}
    return render(request,'polls/index.html',context)