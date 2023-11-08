from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('playlist/<int:id>', views.playlist, name="playlist"),
    path('forms/', views.forms, name="form"),
    path('email/', views.email_page, name="email"),
]
