from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/',views.redgister,name='redgister'),
    path('signin/',LoginView.as_view(template_name='home/signin.html'),name='login'),
]