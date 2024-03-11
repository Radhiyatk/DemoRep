from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.demo,name='demo'),

]