from models import *
from django.forms import ModelForm
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'flag_time', 'flag')

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        exclude = ('create_time', 'creator')
    
