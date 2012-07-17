from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, redirect
from django.template import RequestContext
from forms import *
from models import *
import datetime

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = Feedback()
            feedback.email = form.cleaned_data['email']
            feedback.feedback = form.cleaned_data['feedback']
            feedback.time = datetime.datetime.now()
            feedback.name = form.cleaned_data['name']
            feedback.save()
            return redirect('/feedback/success/')
    else:
        form = FeedbackForm()
    return render_to_response("feedback.html", {'form':form}, context_instance=RequestContext(request))
