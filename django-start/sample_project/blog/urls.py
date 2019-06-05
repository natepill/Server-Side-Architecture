from django.urls import path
from . import views

#urlpatterns[0] : homepage
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
