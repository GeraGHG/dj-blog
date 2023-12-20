from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField("Name project: ", max_length=100)
    description = models.CharField("Description: ", max_length=500)
    image = models.ImageField(upload_to="portfolio/images/")
    url = models.URLField(blank=True)
