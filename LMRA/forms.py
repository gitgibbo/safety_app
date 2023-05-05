from django import forms
from .models import LMRA, Hazard

class LMRAForm(forms.ModelForm):
    class Meta:
        model = LMRA
        fields = ['location']

class HazardForm(forms.ModelForm):
    class Meta:
        model = Hazard
        fields = ['hazard', 'description', 'likelihood', 'severity']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'likelihood': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'severity': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
    likelihood = forms.IntegerField(min_value=1, max_value=5)
    severity = forms.IntegerField(min_value=1, max_value=5)


HazardFormSet = forms.inlineformset_factory(LMRA, Hazard, form=HazardForm, extra=0, can_delete=False)