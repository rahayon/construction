from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from about.models import AboutContent, AboutPromo
from projects.models import Project


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['about_content'] = AboutContent.objects.first()
        context['about_promo'] = AboutPromo.objects.all()
        return context
