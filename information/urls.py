from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ourchurch, name='ourchurch'),
    path('fm/', views.fm, name='fm'),
    path('yi/', views.yi, name='yi'),
    path('mh/', views.mh, name='mh'),
    path('directions/', views.d, name='directions'),
    path('schedule/', views.schedule, name="schedule")
]
