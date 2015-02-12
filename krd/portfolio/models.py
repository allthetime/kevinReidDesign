from django.db import models

class Project(models.Model):
    path            = models.CharField(default="",max_length=256)
    title           = models.CharField(default="",max_length=256)
    tag_line        = models.CharField(default="",max_length=256)
    description     = models.TextField(default="")
    video           = models.URLField(default="")
    project_image   = models.ImageField(upload_to = 'pics', default = 'pics/no-img.jpg')

    def __str__(self):
        return "%s" % self.path

class Image(models.Model):
    project         = models.ForeignKey(Project)
    image           = models.ImageField(upload_to = 'pics', default = 'pics/no-img.jpg')

class Biography(models.Model):
    bio             = models.TextField(default="")
    pic             = models.ImageField(upload_to = 'pics', default = 'pics/no-img.jpg')        
    email           = models.EmailField(default="")
    resume          = models.FileField(upload_to = 'pdf')
