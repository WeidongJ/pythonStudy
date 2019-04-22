# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    string = u'solo social'
    studyList = ['django', 'selenium','linux', 'python']
    return render(request, 'webapp_pruemat/index.html', {'string':string,'studyList':studyList}) # render可以指定变量给html调用 多个变量传给dict


def add(request): 
    a = request.GET['a'] # 获取传入的参数
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a,b)) # reverse 接收 url 中的 name 作为第一个参数 返回url
    )
