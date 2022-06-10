from django.db import models
from django.urls import reverse


class Photography(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photography_detail', args=[self.id])


class Image(models.Model):
    Photography = models.ForeignKey(
        Photography, related_name="image", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/img')
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
