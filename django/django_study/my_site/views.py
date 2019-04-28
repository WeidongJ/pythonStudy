from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,User,Choice
from django.template import loader

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('my_site/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(template))