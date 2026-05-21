from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('buses/', views.bus_list, name='bus_list'),

    path('drivers/', views.driver_list, name='driver_list'),

    path('conductors/', views.conductor_list, name='conductor_list'),

    path('routes/', views.route_list, name='route_list'),

    path('passengers/', views.passenger_list, name='passenger_list'),

    path('locations/', views.bus_location_list, name='bus_location_list'),

    path('schedules/', views.bus_schedule_list, name='bus_schedule_list'),
]