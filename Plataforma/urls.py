from django.urls import path
from Plataforma.views import *

urlpatterns = [
    path('',principal,name="principal"),
    path('login/',login_request,name="login"),
    path('logout/',logout_request,name="logout"),
    path('registro/',registro_request,name="registro"),
    path('<int:user_id>/add_pub/',add_pub,name="add"),
    path('publicaciones/',publicaciones,name="publicaciones"),
    path('ventas/',ventas,name="ventas"),
 ]