from django.test import TestCase

import datetime
from django.utils import timezone

from .models import Question

# Create your tests here.
class QuestionModelsTests(TestCase):

    def test_was_published_recently(self):
        time = timezone.now() +datetime.timedelta(days=30)
        q = Question(pub_date=time)
        self.assertFalse(q.was_published_recently())