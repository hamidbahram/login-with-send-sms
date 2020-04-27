from django.urls import path
from . import views

urlpatterns = [
    path('get_code/', views.get_code, name="get_code"),
    path('chek_code/', views.chek_code, name="chek_code"),
]
