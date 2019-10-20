from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=500)
    

    def __str__(self):
        return self.bio

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=username).all()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to='pics/')
    image_name = models.CharField(max_length=30)
    caption = models.TextField()
    likes = models.ManyToManyField(User)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.description


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()



class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.name} Image'


class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')
    def __str__(self):
        return f'{self.follower} Follow'

