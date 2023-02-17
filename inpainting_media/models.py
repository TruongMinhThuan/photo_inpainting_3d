from django.db import models

# Create your models here.
class MediaModel(models.Model):
    title = models.CharField(max_length=200,null=True)
    prompts = models.CharField(max_length=200,null=True)
    media_file = models.FileField(blank=True, null=True,upload_to='media/',)