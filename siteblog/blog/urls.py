from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('category/<str:slug>/', views.ByCategory.as_view(), name='category'),
    path('post/<str:slug>/', views.GetPost.as_view(), name='post'),
    path('tag/<str:slug>/', views.ByTag.as_view(), name='tag'),
]
