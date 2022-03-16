from django import forms


class AvailabilityForm(forms.Form):
    Unit_Types = (
        ('Mini', 'Mini Unit'),
        ('Medium', 'Medium Unit'),
        ('Large', 'Large Unit'),
    )

    unit_type = forms.ChoiceField(choices=Unit_Types, required=True)
    check_in = forms.DateField(required=True, input_formats=["%d/%m/%y",])
    check_out = forms.DateField(required=True, input_formats=["%d/%m/%y",])
