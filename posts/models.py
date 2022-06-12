from django.db import models
from django.urls import reverse


class Content(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    content = models.CharField(max_length=5000, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content_detail', args=[self.id])


class Image(models.Model):
    image = models.ImageField(upload_to='media/img')
    caption = models.CharField(max_length=128, blank=True)
    title = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    photo = models.ForeignKey(
        Content, related_name="image_img", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Content, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
