from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('contact/', views.contactus, name="contact"),
    path('demo/', views.demo, name="demo"),

]