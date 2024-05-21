from django.urls import path
from . import views

urlpatterns = [
    path('', views.block_list, name='blog_list')
]