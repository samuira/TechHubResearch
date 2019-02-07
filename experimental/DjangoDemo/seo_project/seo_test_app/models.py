from django.db import models
from django.urls import reverse

# Create your models here.


class Drug(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField()
    type = models.CharField(max_length=255, default='')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('seo_drug_edit', args=[str(self.id)])


class Liquor(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField()
    type = models.CharField(max_length=255, default='')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('seo_liquor_edit', args=[str(self.id)])