from django.db import models


# Create your models here.
class AboutContent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class AboutPromo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    icon_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class WorkPlan(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
