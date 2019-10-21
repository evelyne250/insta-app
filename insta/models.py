from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=500)
    name = models.CharField(max_length=120)
    

    def __str__(self):
        return self.name
    @classmethod
    def search_by_name(cls,search_term):
       news = cls.objects.filter(user__username__icontains = search_term)
       return news

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to='pics/')
    image_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="image")
    caption = models.TextField()
    likes = models.IntegerField(default=0)
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.image_name
    
    def addlikes(self):
        self.likes.count()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

  
    @classmethod
    def get_all_images(cls):
        images=cls.objects.all().prefetch_related('comment_set')
        return images

class Comment(models.Model):
    posted_by=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    comment_image=models.ForeignKey(Image,on_delete=models.CASCADE,null=True)
    comment=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.posted_by



class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')
    def __str__(self):
        return f'{self.follower} Follow'

