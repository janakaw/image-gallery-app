from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.get_projects, name='projects-list'),
    path('project_image/', views.get_project_image, name='project-cover-image'),
    path('project_text/', views.get_project_text, name='project-text'),
    path('slider_image_count/', views.get_slider_image_count, name='project-slider-count'),
    path('slider_image/', views.get_slider_image, name='project-slider'),
    path('slider_text/', views.get_slider_text, name='project-slider-text'),
]
