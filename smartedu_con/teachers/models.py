from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length = 50)
    title = models.TextField(blank = True)    
    image = models.ImageField(upload_to="teachers/%Y/%m/%d/",  default="teachers/default_teacher_image.jpg")
    facebook = models.URLField(max_length=100, blank=True)
    twittter = models.URLField(max_length=100, blank=True)
    linkedin = models.URLField(max_length=100, blank=True)
    youtube = models.URLField(max_length=100, blank=True)

    def __str__(self):
        return self.name
