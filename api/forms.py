from django import forms


class DetectionForm(forms.Form):
    image = forms.ImageField()
