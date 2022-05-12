from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('category/<str:slug>', views.category, name='category'),
    path('tag/<str:slug>', views.index, name='tag'),
    path('post/<str:slug>', views.index, name='post'),
]
