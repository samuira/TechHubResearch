from django.db import models
from custom_admin.models import User


class BlogPost(models.Model):
    published_on = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title_image = models.ImageField(upload_to='blog/title_images/%Y/%m/%d', blank=True, null=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    slug = models.SlugField(max_length=300, unique=True)
    is_verified = models.BooleanField(default=False)
