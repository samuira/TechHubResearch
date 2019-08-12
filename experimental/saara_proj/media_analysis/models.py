from django.db import models
from jsonfield import JSONField


# Create your models here.
class ImageStorage(models.Model):
	image = models.ImageField(upload_to='images/%Y/%m/%d', default='')
	analysis_json = JSONField()
	client_ip = models.CharField(max_length=20, default='')
