from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
        email = forms.EmailField(required=True)
        firstname = forms.CharField(max_length=30, required=True)
        lastname = forms.CharField(max_length=30, required=True)
        school = forms.CharField(max_length=40, required=True)
        level = forms.IntegerField(required=True, max_value= 6, min_value=1)
        combination = forms.CharField(max_length=3, required=True)
        

        class Meta:
            model = User
            fields = ("username", "email","firstname","lastname","school","combination","level", "password1", "password2")

        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.firstname = self.cleaned_data['firstname']
            user.lastname = self.cleaned_data['lastname']
            user.school = self.cleaned_data['school']
            user.level = self.cleaned_data['level']
            user.combination = self.cleaned_data['combination']


            if commit:
                user.save()
            return user