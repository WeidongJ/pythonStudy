from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User,Question,Choice

# Choice question字段的外键是Question.question,django.admin.StackedInline指定Question创建时的choice的数量

# class ChoiceInline(admin.StackedInline):大量占据了页面空间
class ChoiceInline(admin.TabularInline): # 关联对象布局
    model = Choice
    extra = 3

# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date','question_text'] #fields 被我拼成了 fields
    # 自定义后台表单描述
    list_display = ('question_text','pub_date','was_published_recently')
    # 添加侧边筛选
    list_filter = ['pub_date']

    # 添加搜索,支持模糊匹配
    search_fields = ['question_text']
    # list_filter = ['question_text']
    fieldsets = [(None, {'fields': ['question_text']}),
    ('日期信息：',{'fields': ['pub_date']}),]
    inlines=[ChoiceInline]



admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(User)

