# App level urls.py file



from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstApp,name='firstApp'),
    path('about/', views.about,name='about'),
]
