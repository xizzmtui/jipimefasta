
from email.errors import NonPrintableDefect
from http.client import HTTPResponse
from multiprocessing import context
from pydoc import describe
from django import db
from django.shortcuts import render

# Create your views here.

from http import server
from itertools import combinations
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from numpy import gradient
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import NotesUser, ReplyReplies, User, Question, Question_Options, Quiz, Quiz_Question, Feedback, ContentSuggested, Post,  Reply, Notes
from .serializers import UserSerializer, QuizSerializer, Quiz_QuestionSerializer, QuestionSerializer, Question_OptionsSerializer,FeedbackSerializer, ContentSuggestedSerializer, PostSerializer, ReplySerializer
from quizapp import serializers
import sqlite3
from .forms import NewUserForm, UserUpdateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.core.paginator import Paginator
from django.views.generic import ListView







# Create your views here.
def test(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3) # Show 3 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'test.html', {'page_obj': page_obj})

@login_required
def userprofile(request, id):
    yuza = User.objects.filter(id=id).values()[0]
    username = yuza['username']
    first_name = yuza['first_name']
    last_name = yuza['last_name']
    date_joined = yuza['date_joined']
    yuza1 = {'username': username, 'first_name': first_name, 'last_name': last_name, 'date_joined':date_joined, 'id':id}
    return render(request, 'userprofile.html', yuza1)

def index(request):
    return render(request,'index.html')

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})
    
@login_required
def forum(request):
    post_list = Post.objects.all().order_by('-date')
    paginator = Paginator(post_list, 10) # Show 3 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'forum.html', {'page_obj': page_obj})

@login_required
def forum_1(request):

    # most replied to
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10) # Show 3 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'forum.html', {'page_obj': page_obj})

@login_required
def forum_2(request):

    # recent replied
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10) # Show 3 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'forum.html', {'page_obj': page_obj})
    
@login_required
def forum_3(request):

    # no reply yet
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10) # Show 3 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'forum.html', {'page_obj': page_obj})

@login_required
def forum_4(request):

    # own posts
    post_list = Post.objects.filter(usr=request.user.id).order_by('-date')
    paginator = Paginator(post_list, 10) # Show 3 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'forum.html', {'page_obj': page_obj})

@login_required
def userposts(request, id):
    post_list = Post.objects.filter(usr=id).order_by('-date')
    paginator = Paginator(post_list, 10) # Show 3 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'forum.html', {'page_obj': page_obj})

@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('dashboard')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }

    return render(request, 'profileupdate.html', context)


@login_required
def profile_view(request):
    return render(request,'dashboard.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("dashboard")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_django(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                if request.POST.get('next') == None:
                    return redirect("dashboard")
                return redirect(request.POST.get('next'))
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})
    

@login_required       
def logout_django(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

@login_required
def makepost(request):
    if request.method == 'POST':
        post_contents = request.POST
        category = post_contents['category']
        title = post_contents['title']
        image = post_contents['ufile']
        content = post_contents['content72']
        Post.objects.create(usr_id = request.user.id ,category=category, title=title, img=image, content=content)
        messages.success(request,'data has been successfuly submitted')
        return redirect('forum')

    return render(request, 'makepost.html')

@login_required 
def viewpost(request, id):
    if request.method == 'POST':
        content = request.POST['reply']
        usr = User.objects.filter(id=request.user.id)[0]
        pid = Post.objects.filter(id=id)[0]
        Reply.objects.create(content=content,usr=usr,pid=pid)
        messages.success(request, 'Reply saved')
        return redirect('viewpost', id=id)
    posts = Post.objects.filter(id=id).values()
    post = posts[0]
    title = post['title']
    img = post['img']
    usr = post['usr_id']
    content = post['content']
    share = post['share']
    date = post['date']
    category = post['category'] 
    post_id = post['id']

    page_obj = Reply.objects.filter(pid=id)
    comment_count = len(page_obj)

    wall = {'id': post_id, 'title': title, 'content': content, 'usr': usr, 'share': share, 'date': date,
            'category': category, 'img': img, 'page_obj': page_obj, 'comment_count': comment_count}
    print(wall)
    return render(request, 'viewpost.html', wall)





@login_required
def rep_rep(request, pid, rid):
    if request.method == 'POST':
        content = request.POST['reply']
        usr = User.objects.filter(id=request.user.id)[0]
        rid = Reply.objects.filter(id=rid)[0]
        ReplyReplies.objects.create(content=content, usr=usr, rid=rid)
        messages.success(request, 'Reply saved')
        return redirect('rep_rep', pid=pid, rid=rid)
    posts = Post.objects.filter(id=pid).values()
    post = posts[0]
    title = post['title']
    img = post['img']
    usr = post['usr_id']
    content = post['content']
    share = post['share']
    date = post['date']
    category = post['category']
    post_id = post['id']

    page_obj = Reply.objects.filter(pid=pid)
    comment_count = len(page_obj)
    reps_rep = ReplyReplies.objects.filter(rid=rid)

    wall = {'id': post_id, 'title': title, 'content': content, 'usr': usr, 'share': share, 'date': date,
            'category': category, 'img': img, 'page_obj': page_obj, 'reps_rep':reps_rep, 'comment_count': comment_count}
    print(wall)
    return (request, 'viewpost.html', wall)


@login_required
def feedback(request):
    if request.method == 'POST':
        content = request.POST['content']
        img = request.POST['ufile']
        Feedback.objects.create(usr=request.user, content=content, img=img)
        messages.success(request, 'Thank you for contacting us')
        return redirect('index')
    return render(request, 'feedback.html')

@login_required
def selectquiz(request):
    if request.method == 'POST':
        form_results = request.POST
        level = form_results['levels']
        subject = form_results['subs']
        quiz_choice = form_results ['quiz']
        request.session['level']=level
        request.session['subject']=subject

        if quiz_choice == 'Challenge Another Student':
            quiz_option = 'h2h'
        elif quiz_choice == 'Survival Quiz':
            quiz_option = 'survival'
        elif quiz_choice == 'Timed Quiz':
            quiz_option = 'normal'
        else:
            quiz_option = 'index'


        return redirect(quiz_option,)


    return render(request, 'selectquiz.html')



@login_required
def h2h(request):
        category = request.session['subject']
        level = request.session['level']
        if level == 'Form 1' :
            levels = 1
        elif level == 'Form 2':
            levels = 2
        elif level == 'Form 3':
            levels = 3
        elif level == 'Form 4':
            levels = 4
        elif level == 'Form 5':
            levels = 5
        else:
            levels = 6

        quest = Question.objects.filter(category=category, level=levels)
        
        quiz = []
        i = 1
        for quez in quest:
            options = Question_Options.objects.filter(qid=quez)
            optionz = []
            for option in options:
                optionz.append(option.option)
            q_dict = {
                "numb": i,
                "question": quez.description,
                "answer": quez.answer,
                "options":optionz
            }

            quiz.append(q_dict)
            print(quiz)
            i+=1
        f = open("quizapp/static/js/test.js", "w")
        f.write("let questions = "+str(quiz))
        f.close()
        return render(request, 'h2h.html')


@login_required
def survival(request):

        category = request.session['subject']
        level = request.session['level']
        if level == 'Form 1' :
            levels = 1
        elif level == 'Form 2':
            levels = 2
        elif level == 'Form 3':
            levels = 3
        elif level == 'Form 4':
            levels = 4
        elif level == 'Form 5':
            levels = 5
        else:
            levels = 6

        quest = Question.objects.filter(category=category, level=levels)
        
        quiz = []
        i = 1
        for quez in quest:
            options = Question_Options.objects.filter(qid=quez)
            optionz = []
            for option in options:
                optionz.append(option.option)
            q_dict = {
                "numb": i,
                "question": quez.description,
                "answer": quez.answer,
                "options":optionz
            }

            quiz.append(q_dict)
            print(quiz)
            i+=1
        f = open("quizapp/static/js/test.js", "w")
        f.write("let questions = "+str(quiz))
        f.close()
        return render(request, 'survival.html')


@login_required
def normal(request):
        category = request.session['subject']
        level = request.session['level']
        if level == 'Form 1' :
            levels = 1
        elif level == 'Form 2':
            levels = 2
        elif level == 'Form 3':
            levels = 3
        elif level == 'Form 4':
            levels = 4
        elif level == 'Form 5':
            levels = 5
        else:
            levels = 6

        quest = Question.objects.filter(category=category, level=levels)
        
        quiz = []
        i = 1
        for quez in quest:
            options = Question_Options.objects.filter(qid=quez)
            optionz = []
            for option in options:
                optionz.append(option.option)
            q_dict = {
                "numb": i,
                "question": quez.description,
                "answer": quez.answer,
                "options":optionz
            }





            quiz.append(q_dict)
            print(quiz)
            i+=1
        f = open("quizapp/static/js/test.js", "w")
        f.write("let questions = "+str(quiz))
        f.close()
        return render(request, 'normal.html')


@login_required
def notes(request, id):
    notesy = Notes.objects.filter(id=id).values()[0]
    return render(request, 'notes.html', notesy)

@login_required
def favnotes(request):
    favnot = NotesUser.objects.filter(yuza=request.user).values()
    notesy = []

    for favnut in favnot:
        print (favnut)
        notez = Notes.objects.filter(id=favnut['fav_id']).values()[0]
        notesy.append(notez)
        print(notesy)
    return render(request, 'favnotes.html', {'notesy':notesy})

@login_required
def selectnotes(request):
    if request.method == 'POST':
        title = request.POST['subs']
        level = request.POST['levels']
        if level == 'Form 1' :
            levels = 1
        elif level == 'Form 2':
            levels = 2
        elif level == 'Form 3':
            levels = 3
        elif level == 'Form 4':
            levels = 4
        elif level == 'Form 5':
            levels = 5
        elif level == 'Form 6':
            levels = 6
        else:
            levels = request.user.id

        notez = Notes.objects.filter(category=title, level=levels).values()[0]
        messages.success(request, 'notes available')
        return render(request,'notes.html', notez)
    return render(request, 'selectnotes.html')

@login_required
def contribute(request):
    return render(request, 'contribute')

def aboutus(request):
    return render(request, 'aboutus.html')


@login_required
def leaderboard(request):
    return render(request, 'leaderboard.html')

@login_required
def make_questions(request):
    if request.method == "POST":
        description = request.POST['content']
        category = request.POST['category']
        level = request.POST['level']
        answer = request.POST['answer']
        answer_description = request.POST['answer_description']

        Question.objects.create(description=description, category=category, level=level, answer=answer, answer_description=answer_description)

        question = Question.objects.filter(description=description, category=category, level=level, answer=answer, answer_description=answer_description)[0]
        # question options
        opt1 = request.POST['opt1']
        opt2 = request.POST['opt2']
        opt3 = request.POST['opt3']
        opt4 = request.POST['opt4']
        Question_Options.objects.create(qid=question, option=opt1)
        Question_Options.objects.create(qid=question, option=opt2)
        Question_Options.objects.create(qid=question, option=opt3)
        Question_Options.objects.create(qid=question, option=opt4)

        messages.success(request,'Question Created')
        return render(request, 'makequestion.html')
    return render(request, 'makequestion.html')

def report(request):
    return render(request, 'report.html')


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
