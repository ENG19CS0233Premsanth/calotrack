from django import forms
from .models import calmodel,dropdo

class calform(forms.ModelForm):
    class Meta:
        model=calmodel
        fields=['name','quantity']

class addcalform(forms.ModelForm):
    class Meta:
        model=calmodel
        fields="__all__"

class dropform(forms.ModelForm):
    class Meta:
        model = dropdo
        fields = ['consumedfood',"quantity"]