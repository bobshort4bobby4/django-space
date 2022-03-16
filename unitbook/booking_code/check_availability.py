import datetime
from unitbook.models import Unit, Booking

def check_availability(unit, check_in, check_out):
    avail_list = []
    bookings = Booking.objects.filter(unit=unit)
    for booking in bookings:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)

    return all(avail_list)
    
