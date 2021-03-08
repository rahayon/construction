from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe


class ProjectCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class ProjectManager(models.Manager):
    def all_categories(self):
        qs = self.get_queryset()
        return qs.select_related('category')

class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='p_category')
    title = models.CharField(max_length=255)
    sub_title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    feature_image = models.ImageField(upload_to='project_image', blank=True)
    architects = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    area = models.FloatField(default=0.00)
    project_start = models.DateField(blank=True)
    project_end = models.DateField(blank=True)
    manufactures = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProjectManager()

    def __str__(self):
        return self.title

    def image_url(self):
        if self.feature_image:
            return self.feature_image.url
        else:
            return ''

    def image_tag(self):
        return mark_safe('<img src="{}" height="70" width="60"/>'.format(self.image_url))

    def get_absolute_url(self):
        return reverse('projects:project-detail', kwargs={'pk': self.pk})


class ProjectImageManager(models.Manager):
    def all_images(self):
        qs = self.get_queryset()
        return qs.select_related('project')
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_image')
    image = models.ImageField(upload_to='project_image', blank=True)
    objects = ProjectImageManager()
    def __str__(self):
        return self.project.title