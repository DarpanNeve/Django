# App level urls.py file



from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='user_home'),
    # path('about/', views.about,name='about'),
    path('<int:user_id>/', views.user_detail,name='user_detail'),
]
