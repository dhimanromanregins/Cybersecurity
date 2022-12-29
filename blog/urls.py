from django.urls import path, include
from . import views



urlpatterns = [
    path('blog/', views.Blogs, name='blog'),
    path('blog_detail/<int:id>', views.BlogDetail, name='blog_detail'),
    path('search/', views.search, name='search')


]