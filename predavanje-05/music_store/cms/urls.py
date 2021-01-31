from django.urls import path

from . import views

urlpatterns = [
    path('pricing/', views.pricing, name='pricing'),
    path('', views.homepage, name='homepage'),

]