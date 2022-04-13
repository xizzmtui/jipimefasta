from asyncio.windows_events import NULL
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Question(models.Model):
    description = models.TextField()
    answer = models.TextField()
    category = models.CharField(max_length=15)
    date = models.DateTimeField(default=datetime.now())
    level = models.IntegerField(default=4)
    answer_description = models.TextField(null=True)

    def __str__(self):
        return self.description


class Question_Options(models.Model):
    qid = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.TextField()

    def __str__(self):
        return self.option


class Quiz(models.Model):
    usr = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    score = models.IntegerField()
    category = models.TextField()
    level = models.IntegerField()
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.category, self.level


class Quiz_Question(models.Model):
    zid = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    qid = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.zid


class Post(models.Model):
    title = models.CharField(max_length=50, default=
    'New Post')
    content = models.CharField(max_length=9999)
    category = models.CharField(max_length=50, blank=True, null=True)
    img = models.ImageField(blank=True, null=True)
    usr = models.ForeignKey(User, on_delete=models.DO_NOTHING)   # id of the sender
    share = models.IntegerField(null=True)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title


class Reply(models.Model):
    pid = models.ForeignKey(Post, on_delete=models.CASCADE)
    usr = models.ForeignKey(
        User, on_delete=models.DO_NOTHING)  # id of the replier
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.pid


class Feedback(models.Model):
    content = models.TextField()
    usr = models.ForeignKey(User, on_delete=models.DO_NOTHING)   # id of the sender
    date = models.DateTimeField(default=datetime.now())
    img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.usr


class ContentSuggested(models.Model):
    q_description = models.TextField()
    q_answer = models.TextField()
    q_options = models.TextField()
    usr = models.ForeignKey(
        User, on_delete=models.DO_NOTHING)   # id of the sender
    date = models.DateTimeField(null=True)
    image = models.ImageField(null=True)
    # notes = models.BinaryField()

    def __str__(self):
        return self.usr

