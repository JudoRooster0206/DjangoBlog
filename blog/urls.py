from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about', views.about, name = 'blog-about'),
    path('about/abouter', views.abouter, name = 'blog-abouter'),
]