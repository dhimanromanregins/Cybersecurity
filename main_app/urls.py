from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path('logout/', views.logout_view, name="logout")
    ]