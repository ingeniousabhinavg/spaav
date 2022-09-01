import imp
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bog/', views.bog, name='bog'),
    path('bwc/', views.bwc, name='bwc'),
    path('commitee/', views.commitee, name='commitee'),
    path('director/', views.director, name='director'),
    path('about/', views.about, name='about'),
    path('achivements/', views.achivements, name='achivements'),
    path('planning/', views.planning, name='planning'),
    path('noticeboard/', views.noticeboard, name='noticeboard'),
    path('tender/', views.tender, name='tender'),
    path('gallery/', views.gallery, name='gallery'),
    path('rti/', views.rti, name='rti'),
    path('policies/', views.policies, name='policies'),
    path('screen-reader-access/', views.screen, name='screen-reader-access'),
]
