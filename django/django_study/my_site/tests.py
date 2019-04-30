from django.test import TestCase,Client

import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question

# Create your tests here.
class QuestionModelsTests(TestCase):

    def test_was_published_recently(self):
        time = timezone.now() +datetime.timedelta(days=30)
        q = Question(pub_date=time)
        self.assertFalse(q.was_published_recently())

    def test_was_published_recently_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1,seconds=1)
        q = Question(pub_date=time)
        self.assertFalse(q.was_published_recently())

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        q = Question(pub_date=time)
        self.assertTrue(q.was_published_recently())

# views test views部分的测试使用代码去测还是依赖人工？
def create_question(question_text,days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(pub_date=time, question_text=question_text)

class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        r = self.client.get(reverse('my_site:index'))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r,'No polls are available.')
        self.assertQuerysetEqual(r.context['qList'],[])

    def test_past_question(self):
        create_question(question_text='Past question',days=-30)
        r = self.client.get(reverse('my_site:index'))
        self.assertQuerysetEqual(r.context['qList'],['<Question: Past question.>'])

    def test_future_question(self):
        create_question(question_text='Future question',days=30)
        r = self.client.get(reverse('my_site:index'))
        self.assertContains(r,'No polls are available.')
        self.assertQuerysetEqual(r.context['qList'],[])

    def test_future_and_past_question(self):
        create_question(question_text='Past question',days=-30)
        create_question(question_text='Future question',days=30)
        r = self.client.get(reverse('my_site:index'))
        self.assertQuerysetEqual(r.context['qList'],['<Question: Past question.>'])

    def test_two_past_question(self):
        create_question(question_text='Past question 1',days=-30)
        create_question(question_text='Past question 2',days=-5)
        r = self.client.get(reverse('my_site:index'))
        self.assertQuerysetEqual(r.context['qList'],['<Question: Past question 2.>', '<Question: Past question 1.>'])