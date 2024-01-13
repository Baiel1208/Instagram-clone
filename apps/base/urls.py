from django.urls import path

from apps.base import views


urlpatterns = [
    path('', views.home, name='home'),
    path('code/', views.code, name='code'),
    path('components/', views.components, name='components'),
    path('explore/', views.explore, name='explore'),
    path('messages/', views.messages, name='messages'),
    path('shop/', views.shop, name='shop'),
    path('upgrade/', views.upgrade, name='upgrade'),

]
