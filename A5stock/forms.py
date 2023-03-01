from django import forms
from .models import PizzaStock

class PizzaForm(forms.ModelForm):
    class Meta:
        model = PizzaStock
        fields = '__all__'