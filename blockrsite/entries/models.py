from django.db import models
from django.contrib.auth.models import User, Permission, Group
from datetime import datetime

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    word_goal = models.IntegerField(default=500)
    hours_per_goal = models.IntegerField(default=5)
    motto = models.CharField(max_length=500, null=True, blank=True)
    flag_time = models.DateTimeField(null=True, blank=True)
    flag = models.BooleanField(default=False)
    github_name = models.CharField(max_length=40, null=True, blank=True)
    commit_goal = models.IntegerField(blank=True, null=True, default=1)
    last_commit_check = models.DateTimeField(null=True, blank=True)
    consecutive_days= models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return self.user.username
    
class Entry(models.Model):
    creator = models.ForeignKey(UserProfile)
    text = models.TextField(null=True, blank=True)
    create_time =models.DateTimeField()
    def __unicode__(self):
        return str(self.create_time)

