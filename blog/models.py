from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_dat = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images')
