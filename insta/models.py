from django.db import models

class Image(models.Model):
    # image = models.ImageField(upload_to='pics/')
    image_name = models.CharField(max_length=30)
    description = models.TextField()
    # location= models.ForeignKey(Location)
    # category = models.ForeignKey(Category, db_column='names')
