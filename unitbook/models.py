from django.db import models
from django.conf import settings


# Create your models here.

class Unit(models.Model):
    Unit_Types = (
        ('Mini', 'Mini Unit'),
        ('Medium', 'Medium Unit'),
        ('Large', 'Large Unit'),
    )

   
    unit_number = models.IntegerField()
    unit_type = models.CharField(max_length=6, choices=Unit_Types)
    capacitycubicm = models.IntegerField()

    def __str__(self):
        return f'{self.unit_number} is a {self.unit_type} unit with a capacity of {self.capacitycubicm} cubic meters'

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.user} has booked {self.unit} from {self.check_in} to {self.check_out}"