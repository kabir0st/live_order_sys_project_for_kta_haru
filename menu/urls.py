from django.urls import path
from . import views

urlpatterns = [
   path('',views.login_user, name="select table"),
   path('<int:table_number>',views.home, name = "home"),
   path('get/menu', views.get_menu, name = "get menu"),
   path('paywithkhalti',views.pay_with_khalti, name="pay with khalti")
]
