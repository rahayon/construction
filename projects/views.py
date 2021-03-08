from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from projects.models import Project


class ProjectDetail(DetailView):
    template_name = 'project/project_detail.html'
    context_object_name = 'single_project'
    queryset = Project.objects.all_categories()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['images'] = Project.project_image.all()
    #     return context
