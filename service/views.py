from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from service.models import Service


class ServiceView(TemplateView):
    template_name = 'service/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context
