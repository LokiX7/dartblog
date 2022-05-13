from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('category/<str:slug>/', views.ByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', views.foo, name='tag'),
    path('post/<str:slug>/', views.foo, name='post'),
]
