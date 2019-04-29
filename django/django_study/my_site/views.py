from django.shortcuts import render,get_object_or_404,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,User,Choice
from django.views import generic

# upgrade views

class IndexView(generic.ListView):
    template_name = 'my_site/index.html'
    context_object_name = 'qList'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Question
    template_name = 'my_site/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'my_site/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request, 'my_site/detail.html',{'question':question,'error_message':'You do not select a choice.',})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('my_site:results',args=(question.id,)))

# Create your views here.
'''def index(request):
    qList = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('my_site/index.html') 导入模版
    context = {
        'qList': qList,
    }
    return render(request, 'my_site/index.html', context) # render函数： 导入模版，关联上下文，返回生成对象,上下文必须是dict
    # return HttpResponse(template.render(context, request)) 返回生成对象

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('question_id not exists')
        
    question = get_object_or_404(Question,pk=question_id) # 使用get_objects_or_404方法抛出异常，目的是为了保证耦合性

    return render(request,'my_site/detail.html',{'question': question})



def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'my_site/results.html',{'question': question})'''