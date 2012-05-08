from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, redirect
from django.template import RequestContext
from forms import *
from django.contrib.auth.decorators import login_required
from models import *
from functions import word_count
import datetime

def check_flag():
    print "starting to check the flag"
    users = UserProfile.objects.all()
    for user in users:
        now = datetime.datetime.now()
        if user.flag_time < now:
            user.flag = False
            user.save()
    print "done checking the flag"
    

def print_something():
    print "something!"

#home page for explaining the extension etc.
def home(request):
    return render_to_response("home.html")

@login_required
def administration(request):
    """
    Allows a user to set the number of words per hour.
    """
    profile = request.user.get_profile()
    person = UserProfile.objects.get(user=profile.user.id)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            person.word_goal = form.cleaned_data['word_goal']
            person.hours_per_goal = form.cleaned_data['hours_per_goal']
            person.motto = form.cleaned_data['motto']
            person.save()
            return redirect('/settings/')
    else:
        form = UserForm()
    return render_to_response("administration.html", {"form":form, "profile":profile}, context_instance=RequestContext(request))

#blank page for writing
def write(request):
    profile = request.user.get_profile()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = Entry()
            entry.text = form.cleaned_data['text']
            entry.creator = UserProfile.objects.get(user=profile.user)
            entry.create_time = datetime.datetime.now()
            entry.save()
            if word_count(entry.text) > profile.word_goal:
                time_delta = datetime.timedelta(hours=profile.hours_per_goal)
                profile.flag_time = entry.create_time + time_delta
                profile.flag = True
                profile.save()
            return redirect('/entries/')
    else:
        form = EntryForm()
    return render_to_response("write.html", {'form':form, 'profile':profile}, context_instance=RequestContext(request))

#list of a users writing
def list(request):
    profile = request.user.get_profile()
    entries = Entry.objects.filter(creator=profile.user)
    return render_to_response("list.html", {'entries':entries})

#view a single bit of writing - should be instantly editable
def view(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render_to_response("view.html", {'entry':entry}, context_instance=RequestContext(request))

#returns a json with a flag
def flag(request):
    profile = request.user.get_profile()
    return render_to_response("flag.html", {'profile':profile}, context_instance=RequestContext(request))