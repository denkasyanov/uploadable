from django.db import models


class Picture(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='pictures')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
