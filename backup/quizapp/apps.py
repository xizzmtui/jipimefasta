from django.apps import AppConfig


class QuizappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quizapp'

    def ready(self):
        import quizapp.signals
