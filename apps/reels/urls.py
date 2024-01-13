from django.urls import path

from apps.reels import views


urlpatterns = [
    path('reels/', views.reels, name='reels'),
    path('reels_view/', views.reels_view, name='reels_view'),
]
