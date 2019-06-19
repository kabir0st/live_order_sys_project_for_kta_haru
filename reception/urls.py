from django.urls import path
from . import views

urlpatterns = [
   path('', views.get_order, name='get order'),
]
