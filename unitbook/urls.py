from django.urls import path
from .views import UnitList, BookingList, BookingView

app_name  = 'unitbook'


urlpatterns = [
    path('unit_list/', UnitList.as_view(), name="UnitList"),
    path('booking_list/', BookingList.as_view(), name="BookingList"),
    path('book/', BookingView.as_view(), name="booking_view"),
]

