from django.db import models


class BlogPost(models.Model):
    published_on = models.DateTimeField(auto_now_add=False, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    title_image = models.ImageField(upload_to='blog/title_images/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    slug = models.CharField(max_length=300, unique=True)
