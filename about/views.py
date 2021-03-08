from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from about.models import AboutContent, AboutPromo, WorkPlan


class AboutUs(TemplateView):
    template_name = 'about/about_us.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_content'] = AboutContent.objects.first()
        context['about_promo'] = AboutPromo.objects.all()
        context['work_plan'] = WorkPlan.objects.all()
        return context
