#Forms is where we deal with HTML forms. Models are database tables.
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        #specify model, User model will change with form.save()
        fields = ['username', 'email', 'password1', 'password2']
        #fields show on form

#A User model form, which is form meant to deal with a certain model
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        #specify model, User model will change with form.save()
        fields = ['username', 'email']
        #fields show on for
        #Profile pic update will be in profile.

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
