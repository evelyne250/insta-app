from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics/')
    image_name = models.CharField(max_length=30)
    caption = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    # location= models.ForeignKey(Location)
    # category = models.ForeignKey(Category, db_column='names')
    def __str__(self):
        return self.description

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.bio