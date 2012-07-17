from models import *
from django.forms import ModelForm
from django import forms

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ('time')
