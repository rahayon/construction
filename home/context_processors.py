from home.models import Settings

def my_settings(request):
    info = Settings.objects.first()
    return {'info':info}