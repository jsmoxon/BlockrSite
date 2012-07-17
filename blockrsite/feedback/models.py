from django.db import models

class Feedback(models.Model):
    email = models.EmailField(null=True, blank=True)
    feedback = models.TextField()
    time = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    def __unicode__(self):
        return self.email
