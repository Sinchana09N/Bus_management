from django.db import models


class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    driver_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    license_number = models.CharField(max_length=50)
    experience_years = models.IntegerField()

    class Meta:
        db_table = 'driver'

    def __str__(self):
        return self.driver_name


class Conductor(models.Model):
    conductor_id = models.AutoField(primary_key=True)
    conductor_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = 'conductor'

    def __str__(self):
        return self.conductor_name

CURRENT_STATUS = [
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('maintenance', 'Under Maintenance'),
]
CROWD_LEVELS = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    ('crowded', 'Crowded'),
]


class Bus(models.Model):

    bus_number = models.CharField(max_length=20)
    
    capacity = models.IntegerField(default=50)

    current_passengers = models.IntegerField(default=0)

    crowd_level = models.CharField(
        max_length=20,
        choices=CROWD_LEVELS,
        default='low'
    )

    is_delayed = models.BooleanField(default=False)
    delay_minutes = models.IntegerField(default=0)

    driver = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        null=True
    )

    conductor = models.ForeignKey(
        Conductor,
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        db_table = 'bus'

    def __str__(self):
        return self.bus_number


class Route(models.Model):
    route_id = models.AutoField(primary_key=True)
    source_place = models.CharField(max_length=100)
    destination_place = models.CharField(max_length=100)
    distance_km = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'route'

    def __str__(self):
        return f"{self.source_place} → {self.destination_place}"


class BusRoute(models.Model):
    bus_route_id = models.AutoField(primary_key=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()

    class Meta:
        db_table = 'bus_route'

    def __str__(self):
        return f"{self.bus} on {self.route}"


class Passenger(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    passenger_id = models.AutoField(primary_key=True)
    passenger_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.IntegerField()

    class Meta:
        db_table = 'passenger'

    def __str__(self):
        return self.passenger_name


class Ticket(models.Model):

    passenger = models.ForeignKey(
        Passenger,
        on_delete=models.CASCADE
    )

    bus = models.ForeignKey(
        Bus,
        on_delete=models.CASCADE
    )

    seat_number = models.IntegerField()

    journey_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
        def save(self, *args, **kwargs):

        is_new = self.pk is None

        super().save(*args, **kwargs)

        if is_new:

            if not hasattr(self.bus, 'current_passengers'):
                self.bus.current_passengers = 0

            self.bus.current_passengers += 1

            percentage = (
                self.bus.current_passengers / 50
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
# class Payment(models.Model):
#     PAYMENT_METHODS = [
#         ('Cash', 'Cash'),
#         ('UPI', 'UPI'),
#         ('Card', 'Card'),
#         ('Net Banking', 'Net Banking'),
#     ]
    
#     payment_id = models.AutoField(primary_key=True)
#     ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
#     payment_date = models.DateField(auto_now_add=True)
#     amount = models.DecimalField(max_digits=8, decimal_places=2)
#     payment_method = models.CharField(max_length=30, choices=PAYMENT_METHODS)

#     class Meta:
#         db_table = 'payment'

#     def __str__(self):
#         return f"Payment {self.payment_id} for Ticket {self.ticket_id}"


# Optional tables
class BusStop(models.Model):
    stop_id = models.AutoField(primary_key=True)
    stop_name = models.CharField(max_length=100)
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        default=0.0
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        default=0.0
    )

    class Meta:
        db_table = 'bus_stop'

    def __str__(self):
        return self.stop_name


class RouteStop(models.Model):
    route_stop_id = models.AutoField(primary_key=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop = models.ForeignKey(BusStop, on_delete=models.CASCADE)
    stop_order = models.IntegerField()
    average_wait_minutes = models.IntegerField(default=0)
    class Meta:
        db_table = 'route_stop'
        ordering = ['stop_order']

    def __str__(self):
        return f"{self.route} - Stop {self.stop_order}: {self.stop}"

class BusLocation(models.Model):
    bus = models.OneToOneField(Bus, on_delete=models.CASCADE)

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    speed = models.FloatField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bus_location'

class BusSchedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    start_time = models.TimeField()
    end_time = models.TimeField()

    frequency_minutes = models.IntegerField()
# Create your models here.
