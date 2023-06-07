from django.core.validators import MinValueValidator
from django.forms import ModelForm, fields, forms

from .models import Person


class TriangleForm(forms.Form):
    leg1 = fields.FloatField(label="Leg 1", validators=[MinValueValidator(0.0000000000000000001)])
    leg2 = fields.FloatField(label='Leg 2', validators=[MinValueValidator(0.0000000000000000001)])


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
