from django import forms
from .models import UserProfile, Preference
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileForm(forms.ModelForm):
    preferences = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Preference.objects.all())
    class Meta():
        model = UserProfile
        fields = ('description','preferences','profile_pic')