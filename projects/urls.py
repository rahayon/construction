from django.urls import path

from projects import views

app_name = 'projects'

urlpatterns = [
    path('<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
]
