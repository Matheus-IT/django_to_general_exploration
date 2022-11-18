from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view),
    path('download_view/', views.download_view, name='download_view'),
]
