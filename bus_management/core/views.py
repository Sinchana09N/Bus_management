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
    
def save(self, *args, **kwargs):

    is_new = self.pk is None

    super().save(*args, **kwargs)

    if is_new:

        self.bus.current_passengers += 1

        percentage = (
            self.bus.current_passengers /
            self.bus.capacity
        ) * 100

        if percentage <= 25:
            self.bus.crowd_level = 'low'

        elif percentage <= 50:
            self.bus.crowd_level = 'medium'

        elif percentage <= 80:
            self.bus.crowd_level = 'high'

        else:
            self.bus.crowd_level = 'crowded'

        self.bus.save()