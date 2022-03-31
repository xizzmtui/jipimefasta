from  django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getUser/',views.UserList.as_view(), name='User' ),
    path('getQuestion/', views.QuestionList.as_view(), name='Question'),
    path('getQuestion_Options/', views.Question_OptionsList.as_view(), name='QO'),
    path('getQuiz/', views.QuizList.as_view(), name='Quiz'),
    path('getQuizQ/', views.Quiz_QuestionList.as_view(), name='QQ'),
    path('getFeedback/', views.FeedbackList.as_view(), name='Feedback'),
    path('getContentSuggested/', views.ContentSuggestedList.as_view(), name='CSugg'),
    path('getPost/', views.PostList.as_view(), name='PostList'),
    path('getReply/', views.ReplyList.as_view(), name='ReplyList'),

#  routes to other web functionalities
    path('forum/', views.forum, name='forum'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('makepost/', views.makepost, name='makepost'),
    path('feedback/', views.feedback, name='feedback'),
    path('selectquiz/', views.selectquiz, name='selectquiz'),
    path('h2h/', views.h2h, name='h2h'),
    path('survival/', views.survival, name='survival'),
    path('normal/', views.normal, name='normal'),
    path('notes/', views.notes, name='notes'),
    path('contribute/', views.contribute, name='contribute'),

    
]