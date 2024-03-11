
from django.urls import path
from registerapp import views, admin

urlpatterns = [

    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

]
