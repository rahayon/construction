from django import template

from home.models import Settings

register = template.Library()


@register.simple_tag
def my_settings():
    setting = Settings.objects.first()
    print("home: ", setting.phone)
    return setting

