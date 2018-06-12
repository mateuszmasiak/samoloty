from django import forms
from models import *

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('first_name','second_name','places_purchased')
