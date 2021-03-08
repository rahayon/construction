from django.contrib import admin
from projects.models import ProjectCategory, Project, ProjectImage


class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage


@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'created_at', 'updated_at']
    list_filter = ['created_at']
    inlines = [ProjectImageAdmin]

    class Meta:
        model = Project


admin.site.register(ProjectCategory)
