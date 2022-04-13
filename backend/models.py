from distutils.command.upload import upload
from django.db import models

class Post(models.Model):
    nomi=models.CharField(max_length=20)
    image1=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nomi
