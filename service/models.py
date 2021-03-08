from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon_name = models.CharField(max_length=50)

    def __str__(self):
        return self.title
