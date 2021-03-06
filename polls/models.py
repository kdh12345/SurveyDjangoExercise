import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date>=timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field= 'pub_date'
    was_published_recently.boolean=True
    was_published_recently.short_description= 'Published recently?'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=220)
    votes = models.IntegerField(default=0)  # 아무것도 투표안한 상태에서는 votes값 0

    def __str__(self):
        return self.choice_text

