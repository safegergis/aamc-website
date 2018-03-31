from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.announcements, name='announcements'),
    path('<int:id>',views.post, name="post")
]