from django.urls import path
from . import views

urlpatterns = [
    path('credits/', views.credits_view, name="credits"),
    path('about/', views.about_view, name="about"),
]
