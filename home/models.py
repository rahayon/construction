from django.db import models


# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=100)
    header_logo = models.ImageField(upload_to='Logo', blank=True)
    footer_logo =models.ImageField(upload_to='Logo', blank=True)
    favicon =models.ImageField(upload_to='Logo', blank=True)
    description = models.TextField(blank=True)
    company = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



