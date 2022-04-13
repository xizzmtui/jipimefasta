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
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_django, name='login'),
    path('register/', views.register, name='register'),
    path('makepost/', views.makepost, name='makepost'),
    path('viewpost/', views.viewpost, name='viewpost'),
    path('feedback/', views.feedback, name='feedback'),
    path('selectquiz/', views.selectquiz, name='selectquiz'),
    path('h2h/', views.h2h, name='h2h'),
    path('survival/', views.survival, name='survival'),
    path('normal/', views.normal, name='normal'),
    path('notes/', views.notes, name='notes'),
    path('contribute/', views.contribute, name='contribute'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('logout/', views.logout_django, name='logout'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('profile_view/',views.profile_view, name='profile_view'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)