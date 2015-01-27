from django.db import models

class Project(models.Model):
    name        = models.TextField(default="")
    description = models.TextField(default="")
    video       = models.URLField(default="")

class Image(models.Model):
    project    = models.ForeignKey(Project)
    image      = models.ImageField(upload_to = '/static/pics', default = '/static/pics/no-img.jpg')
    front_page = models.BooleanField(default=1)

class Biography(models.Model):
    bio    = models.TextField(default="")
    resume = models.FileField(upload_to = '/static/pdf')
    email  = models.EmailField(default="")
