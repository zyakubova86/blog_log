from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    img = models.ImageField(verbose_name='Photo', upload_to='posts_img/', blank=True, null=True)

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default="admin")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.title


class Meta:
    ordering = ('-created',)
    verbose_name = "Post"
    verbose_name_plural = "Posts"
