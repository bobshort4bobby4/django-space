from django.shortcuts import render, HttpResponse
from django.views.generic import ListView ,FormView
from .models import Unit, Booking
from .forms import AvailabilityForm
from .booking_code.check_availability import check_availability

# Create your views here.
class UnitList(ListView):
    model = Unit

class BookingList(ListView):
    model = Booking

class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'
    def form_valid(self,form):
        data = form.cleaned_data
        unit_list = Unit.objects.filter(unit_type=data['unit_type'])
        free_units =[]
        for unit in unit_list:
            if check_availability(unit, data['check_in'], data['check_out']):
                free_units.append(unit)
        if len(free_units) >0:
            unit = free_units[0]
            booking = Booking.objects.create(
                user = self.request.user,
                unit = unit,
                check_in = data['check_in'],
                check_out = data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('this unit size are all booked up for your required time period')

