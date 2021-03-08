from home.models import Settings

def my_settings(request):
    return Settings.objects.first()