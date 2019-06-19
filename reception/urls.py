from django.urls import path
from . import views

urlpatterns = [
   path('', views.get_order, name='get order'),
   path('/<int:id>/',views.order_done, name = "order done")
]
