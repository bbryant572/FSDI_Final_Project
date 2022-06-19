from django.db import models
from django.urls import reverse

class Account(models.Model):
    image = models.ImageField(upload_to='media/img')
    # for the username, how do we add the one they have already created?
    username = models.CharField(max_length=75, blank=False)
    name = models.CharField(max_length=255, blank=True)
    about = models.CharField(max_length=400, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user_profile', args=[self.id])
