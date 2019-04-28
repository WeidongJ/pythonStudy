from django.db import models

# Create your models here.
# 用户表
class User(models.Model):
    id = models.AutoField(int(11), primary_key=True)
    name = models.CharField(max_length = 30, default=None)
    email = models.EmailField(max_length = 32, null=True)
    avatar = models.ImageField(null=True, blank=True, default=None)
    ctime = models.DateTimeField(auto_now=True)
    uptime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name # 指定User.objects.all()时返回值

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)





