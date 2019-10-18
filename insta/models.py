from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics/')
    post = HTMLField()
    image_name = models.CharField(max_length=30)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    # location= models.ForeignKey(Location)
    # category = models.ForeignKey(Category, db_column='names')
    def __str__(self):
        return self.description