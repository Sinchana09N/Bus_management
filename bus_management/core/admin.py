from django.contrib import admin
from .models import *

admin.site.register(Driver)
admin.site.register(Conductor)
admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(BusRoute)
admin.site.register(Passenger)
admin.site.register(Ticket)
# admin.site.register(Payment)
