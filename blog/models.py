from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description')
    image = models.ImageField(upload_to='blog/images')
    date = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.title
