from tkinter.ttk import OptionMenu
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# Create your forms here.

class NewUserForm(UserCreationForm):
        email = forms.EmailField(required=True)
        school = forms.CharField(max_length=40, required=True)
        level = forms.IntegerField(required=True, max_value= 6, min_value=1)
        combination = forms.CharField(max_length=3, required=True)
        

        

        class Meta:
            model = User
            fields = ("username", "email","first_name","last_name","school","combination","level", "password1", "password2",)

        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.school = self.cleaned_data['school']
            user.level = self.cleaned_data['level']
            user.combination = self.cleaned_data['combination']


            if commit:
                user.save()
            return user

# Create a UserUpdateForm to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    school = forms.CharField()
    level = forms.IntegerField()
    combination = forms.CharField()
    username = User.username
    

    class Meta:
        model = User
        fields = ['username', 'email',  'firstname', 'lastname', 'school', 'level', 'combination']
        


