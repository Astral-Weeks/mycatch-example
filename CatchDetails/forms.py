from django.forms import ModelForm
from django.db import models
from .models import Catch
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class CatchForm(ModelForm):
    class Meta:
        model = Catch
        fields = ["species", "subspecies", "length", "length_guessed",
                  "weight", "weight_guessed", "date", "tag_status", "taken_or_released_status",
                  "river", "photo"]
        widgets = {
            'date': DateInput(),
            'species': forms.Select(attrs={"hx-get": "load_subspecies", "hx-target": "#id_subspecies"})
        }