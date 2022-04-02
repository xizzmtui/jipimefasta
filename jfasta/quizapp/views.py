from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

from http import server
from itertools import combinations
from pyexpat.errors import messages
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from numpy import gradient
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import User, Question, Question_Options, Quiz, Quiz_Question, Feedback, ContentSuggested, Post,  Reply
from .serializers import UserSerializer, QuizSerializer, Quiz_QuestionSerializer, QuestionSerializer, Question_OptionsSerializer,FeedbackSerializer, ContentSuggestedSerializer, PostSerializer, ReplySerializer
from quizapp import serializers


# Create your views here.
def index(request):
    return render(request,'index.html')

def forum(request):
    return render(request, 'forum.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def makepost(request):
    return render(request, 'makepost.html')

def viewpost(request):
    return render(request, 'viewpost.html')

def feedback(request):
    return render(request, 'feedback.html')

def selectquiz(request):
    return render(request, 'selectquiz.html')

def h2h(request):
    return render(request, 'h2h.html')

def survival(request):
    return render(request, 'survival.html')

def normal(request):
    return render(request, 'normal.html')

def notes(request):
    return render(request, 'notes.html')

def contribute(request):
    return render(request, 'contribute')

def aboutus(request):
    return render(request, 'aboutus.html')

def leaderboard(request):
    return render(request, 'leaderboard.html')




# API views

class UserList(APIView):
    def get(self, request):
        User1 = User.objects.all()
        serializer = UserSerializer(User1, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




class QuestionList(APIView):
    def get(self, request):
        Question1 = Question.objects.all()
        serializer = QuestionSerializer(Question1, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        


class Question_OptionsList(APIView):
    def get(self, request):
        Question_Option = Question_Options.objects.all()
        serializer = Question_OptionsSerializer(Question_Option, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = Question_OptionsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class QuizList(APIView):
    def get(self, request):
        Quiz1 = Quiz.objects.all()
        serializer =QuizSerializer(Quiz1, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = QuizSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



class Quiz_QuestionList(APIView):
    def get(self, request):
        QuizQ = Quiz_Question.objects.all()
        serializer = Quiz_QuestionSerializer(QuizQ, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = Quiz_QuestionSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class FeedbackList(APIView):
    def get(self, request):
        Fdb = Feedback.objects.all()
        serializer = FeedbackSerializer(Fdb, many=True)
        return Response(serializer.data)


    def post(self, request):
        data = JSONParser().parse(request)
        serializer = FeedbackSerializer(data=data)

        if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ContentSuggestedList(APIView):
    def get(self, request):
        CSugg = ContentSuggested.objects.all()
        serializer = ContentSuggestedSerializer(CSugg, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer= ContentSuggestedSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

class PostList(APIView):
    def get(self,  request):
        NewPost = Post.objects.all()
        serializer = PostSerializer(NewPost, many=True)
        return Response(serializer.data)
        

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class ReplyList(APIView):
    def get(self, request):
        NewReply = Reply.objects.all()
        serializer = ReplySerializer(NewReply, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ReplySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# Other Views