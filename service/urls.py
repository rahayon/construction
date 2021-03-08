from django.urls import path

from service import views

app_name = 'service'

urlpatterns = [
    path('', views.ServiceView.as_view(), name='service'),
]