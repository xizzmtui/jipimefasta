from dataclasses import fields
from rest_framework import serializers
from .models import ContentSuggested, Feedback, Post, Question, Question_Options, Quiz, Quiz_Question, Reply, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class Question_OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question_Options
        fields = "__all__"


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"


class Quiz_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz_Question
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"


class ContentSuggestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentSuggested
        fields = "__all__"
