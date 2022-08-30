import imp
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('planning/', views.planning, name='planning'),
    path('noticeboard/', views.noticeboard, name='noticeboard'),
    path('gallery/', views.gallery, name='gallery'),
    path('rti/', views.rti, name='rti'),
    path('policies/', views.policies, name='policies'),
    path('screen-reader-access/', views.screen, name='screen-reader-access'),
]
