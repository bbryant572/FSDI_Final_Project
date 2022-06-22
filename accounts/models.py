from operator import truediv
from django.db import models
from django.urls import reverse
from django.conf import settings


class Account(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT, blank=True, null=True
    )
    image = models.ImageField(upload_to='media/img')
    # for the username, how do we add the one they have already created?
    username = models.CharField(max_length=75, blank=False)
    email = models.CharField(max_length=255, blank=True)
    about = models.CharField(max_length=400, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/media/img/overlook1.JPG"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user_profile', args=[self.id])
