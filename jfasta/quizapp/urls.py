from  django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .  import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.index, name='index'),
    # path('accounts/', include('django.contrib.auth.urls')), #password reset views
    path('password_reset', views.password_reset_request, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'), 

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
    path('forum1/', views.forum_1, name='forum1'),
    path('forum2/', views.forum_2, name='forum2'),
    path('forum3/', views.forum_3, name='forum3'),
    path('forum4/', views.forum_4, name='forum4'),
    path('forum5/<str:category>/', views.forum_5, name='forum5'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_django, name='login'),
    path('register/', views.register, name='register'),
    path('makepost/', views.makepost, name='makepost'),
    path('viewpost/<int:id>/', views.viewpost, name='viewpost'),
    path('editpost/<int:id>/', views.editpost, name='editpost'),
    path('delete_post/<int:id>/', views.deletepost, name='delete_post'),
    path('feedback/', views.feedback, name='feedback'),
    path('selectquiz/', views.selectquiz, name='selectquiz'),
    path('h2h/', views.h2h, name='h2h'),
    path('survival/', views.survival, name='survival'),
    path('history/<int:id>/', views.history, name='history'),
    path('normal/', views.normal, name='normal'),
    path('notes/<int:id>/', views.notes, name='notes'),
    path('favnotes/', views.favnotes, name='favnotes'),
    path('selectnotes/', views.selectnotes, name='selectnotes'),
    path('contribute/', views.contribute, name='contribute'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('logout/', views.logout_django, name='logout'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('profile_view/',views.profile_view, name='profile_view'),
    path('test/', views.test, name='test'),
    path('userprofile/<int:id>', views.userprofile, name='userprofile'),
    path('makequestion/', views.make_questions, name='makequestion'),
    path('userposts/<int:id>', views.userposts, name='userposts'),
    path('history_details/<int:id>/', views.history_details, name='history_details'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)