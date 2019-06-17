import datetime
from django.utils import timezone

from django.db import models

# NOTE: About database Migrations
# Migrations are very powerful and let you change your models over time,
# as you develop your project, without the need to delete your database or tables
# and make new ones - it specializes in upgrading your database live, without losing data.


# NOTE Three-step guide to making model changes:
# Change your models (in models.py).
# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.


class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    # note a relationship is defined, using ForeignKey. That tells Django each Choice is related to a single Question.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
