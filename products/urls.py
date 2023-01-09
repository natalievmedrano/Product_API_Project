from django.urls import path 
from . import views

urlpatterns = [
    path('', views.product_list),
    path('<pk>/', views.product_detail),
]