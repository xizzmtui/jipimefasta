from django.contrib import admin
from quizapp.models import ContentSuggested, Feedback, Post, Question, Question_Options, Quiz, Quiz_Question, Reply, Profile

# # Register your models here.

admin.site.register(Question)
admin.site.register(Question_Options)
admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Quiz)
admin.site.register(Quiz_Question)
admin.site.register(ContentSuggested)
admin.site.register(Feedback)
admin.site.register(Profile)
