from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'home.html')


def bus_list(request):
    buses = Bus.objects.all()

    context = {
        'buses': buses
    }

    return render(request, 'bus_list.html', context)


def driver_list(request):
    drivers = Driver.objects.all()

    context = {
        'drivers': drivers
    }

    return render(request, 'driver_list.html', context)


def conductor_list(request):
    conductors = Conductor.objects.all()

    context = {
        'conductors': conductors
    }

    return render(request, 'conductor_list.html', context)


def route_list(request):
    routes = Route.objects.all()

    context = {
        'routes': routes
    }

    return render(request, 'route_list.html', context)


def passenger_list(request):
    passengers = Passenger.objects.all()

    context = {
        'passengers': passengers
    }

    return render(request, 'passenger_list.html', context)


def bus_location_list(request):
    locations = BusLocation.objects.all()

    context = {
        'locations': locations
    }

    return render(request, 'bus_location_list.html', context)


def bus_schedule_list(request):
    schedules = BusSchedule.objects.all()

    context = {
        'schedules': schedules
    }

    return render(request, 'bus_schedule_list.html', context)
    
