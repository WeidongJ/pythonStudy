# Django 学习笔记 
learn from [django][]  开始于2019/04/29



## 主要问题
* django转码问题
* 抄代码粗心：把%炒成&
* 定位问题粗心

## 主要内容
### views
1. render函数：导入模版，关联上下文（交互？），返回生成的对象；**context必须是dict**

    return render(request, 'my_site/index.html', context)


2. 使用函数抛出404异常：不自己抛出异常是为了低耦合设计，受控的耦合存于       django.shortcuts模块里面
### urls
1. 为url指定name参数，views有改动时可以随时改动，方便解耦

    path('',views.index, name='index'),
2. 命名空间：众多应用时为url指定namespace可以解决url冲突问题

    app_name = 'my_site'
### templates
1. 去除模版中的硬编码url，使用低耦合的url name及namespace
        
        <li><a href="{% url 'my_site:detail' question.id %}">{{ question.question_text }}</a></li>


[django]: 'https://docs.djangoproject.com/zh-hans/2.2' "django2.2中文官方文档"