from django import forms
from .models import Chaivarity

class ChaivarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(
        queryset=Chaivarity.objects.all(),
        label="Select chai variety"
    )

    