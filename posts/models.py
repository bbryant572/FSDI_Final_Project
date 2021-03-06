from django.db import models
from django.urls import reverse


class Content(models.Model):
    CHOICES = (
        ('playas del Coco', 'Playas del Coco'),
        ('playa ocotal', 'Playa Ocotal'),
        ('playa hermosa', 'Playa Hermosa'),
        ('marino ballena', 'Marino Ballena'),
    )

    title = models.CharField(max_length=128, null=False, choices=CHOICES)
    text = models.TextField()
    content = models.CharField(max_length=5000, null=True)
    photo = models.ImageField(upload_to='media/img', null=True, blank=True)
    cover = models.FileField(upload_to='media/img', null=True, blank=True)

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/media/img/overlook1.JPG"

    @property
    def get_cover_url(self):
        if self.cover and hasattr(self.cover, 'url'):
            return self.cover.url
        else:
            return "/media/img/writings01.JPG"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content_detail', args=[self.id])


class Image(models.Model):
    # classification =
    image = models.ImageField(upload_to='media/img')
    caption = models.CharField(max_length=128, blank=True)
    title = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    post_linked = models.ForeignKey(
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
