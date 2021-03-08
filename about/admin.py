from django.contrib import admin

# Register your models here.
from about.models import AboutContent, AboutPromo, WorkPlan

admin.site.register(AboutContent)
admin.site.register(AboutPromo)
admin.site.register(WorkPlan)