from django.db import models

# Create your models here.
# schema of database  - structure of data base tables 
# About Model

class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

# Service Model
class Service(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Service name")
    description = models.TextField(verbose_name = "About service")

    def __str__(self):
        return self.name

# Recent work / Projects Model
class RecentWork(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Project Title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title

# Client Model
class Client(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Client name")
    description =  models.TextField(verbose_name = "Client say")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name